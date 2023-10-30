<template>
    <main>
        <div v-if="!loading">
            <div class="m-7 flex justify-between">
                <div class="bg-gray-300 rounded-md p-7 w-max">
                    <h2 class="h2-c mb-3">Load an existing dataset or create a new one</h2>
                    <div class="justify-center [&>button]:ml-6 flex ">
                        <button class="form-button" @click="toggleLoadModal">Load quiz</button>
                        <button class="form-button" @click="toggleCreateModal">Create new quiz</button>
                    </div>
                </div>
                <div class="bg-gray-300 rounded-md p-7 w-max">
                    <h2 class="h2 mb-3">Datasets:</h2>
                    <div v-if="datasets == 0">
                        <span class="text-gray-500">No datasets</span>
                    </div>
                    <div v-else>
                        <ul>
                            <li v-for="quiz in quizzes" :key="quiz">{{ quiz }}</li>
                        </ul>

                    </div>
                </div>
            </div>
        </div>
        <div v-else>
            <div>
                <span class="loader"></span>
            </div>
        </div>

        <!-- Create-a-new-quiz-modal -->
        <fwb-modal size="7xl" v-if="createModal" class="max-w-7xl">
            <template #header>
                <div class="w-full">
                    <h2 class="h2-c">Create a new quiz</h2>
                    <button type="button" @click="toggleCreateModal"
                        class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-snytext rounded-lg text-sm w-8 h-8 ml-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white">
                        <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                            viewBox="0 0 14 14">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
                        </svg>
                        <span class="sr-only">Close modal</span>
                    </button>
                </div>
            </template>
            <template #body>
                <div class="w-full">
                    <form @submit.prevent="" class="md:w-full">
                        <div class="flex flex-row bg-neutral-50">
                            <div class="flex-col justify-start mr-5">
                                <div>
                                    <label for="quizType" class="font-semibold md:text-lg">Quiz type</label>
                                    <select name="quizType" id="quizType" class="form-input" v-model="quizType">
                                        <option value="None">--Select</option>
                                        <option value="MCQ">Multiple choice</option>
                                        <option value="TF">True or false</option>
                                        <option value="FITB">Fill in the blanks</option>
                                        <option value="TA">Typed answer</option>
                                    </select>
                                </div>
                                <div>
                                    <label for="quizSeparator" class="font-semibold md:text-lg">Quiz type</label>
                                    <select name="quizSeparator" id="quizSeparator" class="form-input"
                                        v-model="quizSeparator" @change="changeSeparator">
                                        <option value="None">--Select</option>
                                        <option value="dash">Dash (-)</option>
                                        <option value="equals">Equals (=)</option>
                                        <option value="colon">Colon (:)</option>
                                        <option value="semicolon">Semicolon (;)</option>
                                        <option value="tab">Tab (&RightArrowBar;)</option>
                                    </select>
                                </div>
                                <div>
                                    <label for="quizName" class="font-semibold md:text-lg">Quiz name</label>
                                    <input type="text" class="form-input" name="quizname" id="quizName"
                                        placeholder="Type quiz name here..." v-model="quizName">
                                </div>
                            </div>
                            <div>
                                <label for="quizDescription" class="font-semibold md:text-lg">Quiz description
                                    (optional)</label>
                                <textarea name="quizDescription" id="quizDescription" cols="30" rows="10" class="form-input"
                                    placeholder="Type quiz description here..." v-model="quizDescription"></textarea>
                            </div>
                            <div v-if="errortext">
                                <span class="text-red-500 font-semibold">Error: {{ errortext }}</span>
                            </div>
                            <div v-if="!manualFields" class="ml-auto">
                                <div class="[&>*]:text-green-500">
                                    <h3 class="h3">Guide to importing files</h3>
                                    <fwb-tabs v-model="activeTab" class="p-5">
                                        <fwb-tab name="TA" title="Typed Answer (TA)">
                                            Create a text file (.txt) and write your questions and answers in the following
                                            format:
                                            <br>
                                            <br>
                                            <p class="font-mono">
                                                Question 1 &lt;separator&gt; Answer 1<br>
                                                Question 2 &lt;separator&gt; Answer2<br>
                                                etc...
                                            </p>
                                            <br>
                                            Separators can be any of the following: <code>-</code>, <code>=</code>,
                                            <code>;</code>, <code>:</code>, <code>TAB</code> <br>
                                            Questions and answer pairs should be separated by a newline.
                                        </fwb-tab>
                                        <fwb-tab name="MCQ" title="Multiple Choice (MCQ)">
                                            Create a text file (.txt) and write your questions and answers in the following
                                            format:
                                            <br><br>
                                            <p class="font-mono">
                                                Question 1 &lt;separator&gt; [Answer, WrongAnswer1, WrongAnswer2,
                                                WrongAnswer3] <br>
                                                Question 2 &lt;separator&gt; [Answer, WrongAnswer1, WrongAnswer2,
                                                WrongAnswer3] <br>
                                                etc...
                                            </p>
                                            <br>
                                            Separators can be any of the following: <code>-</code>, <code>=</code>,
                                            <code>;</code>, <code>:</code>, <code>TAB</code> <br>
                                            Questions and answer pairs should be separated by a newline.
                                        </fwb-tab>
                                        <fwb-tab name="TF" title="True or False (TF)">
                                            Create a text file (.txt) and write your questions and answers in the following
                                            format:
                                            <br><br>
                                            <p class="font-mono">
                                                Question 1 &lt;separator&gt; T <br>
                                                Question 2 &lt;separator&gt; F <br>
                                                etc...
                                            </p>
                                            <br>
                                            Separators can be any of the following: <code>-</code>, <code>=</code>,
                                            <code>;</code>, <code>:</code>, <code>TAB</code> <br>
                                            Questions and answer pairs should be separated by a newline.
                                        </fwb-tab>
                                        <fwb-tab name="FITB" title="Fill in the Blanks (FITB)">
                                            Create a text file (.txt) and write your questions and answers in the following
                                            format:
                                            <br><br>
                                            <p class="font-mono">
                                                Question ___ &lt;separator&gt; 1 <br>
                                                I ___ feeling &lt;separator&gt; gotta <br>
                                                etc...
                                            </p>
                                            Separators can be any of the following: <code>-</code>, <code>=</code>,
                                            <code>;</code>, <code>:</code>, <code>TAB</code> <br>
                                            Questions and answer pairs should be separated by a newline. <br>
                                            The gaps in the questions should be represented by 3 underscores.
                                        </fwb-tab>
                                    </fwb-tabs>
                                </div>
                            </div>
                            <div v-else class="ml-[10%]">
                                <ol class="list-disc">
                                    <li class="list-item" v-for="pair in userFields"> Q:{{ pair!.Q }} {{ dispSeparator }}
                                        A:{{ pair!.A }}</li>
                                </ol>
                            </div>
                        </div>
                        <div class="flex flex-row items-center mt-2 [&>*]:mb-0">
                            <button @click="switchButton" class="form-button mt-[2%] h-fit">
                                <span v-if="manualFields" class="text-white font-semibold">Import from
                                    file</span>
                                <span v-else class="text-white font-semibold">Add manually</span>
                            </button>
                            <div v-if="manualFields" class="flex justify-start ml-[5%] mr-auto">
                                <div>
                                    <form @submit.prevent="addFields">
                                        <div class="flex flex-row justify-evenly align-center [&>*]:mx-3">
                                            <div class="flex-col">
                                                <label for="fieldkey">Key</label>
                                                <input type="text" name="fieldkey" id="fieldkey" class="form-input"
                                                    v-model="tbaFieldkey">
                                            </div>
                                            <div class="text-2xl font-extrabold h-fit mb-2 mt-auto">:</div>
                                            <div class="flex-col">
                                                <label for="fieldvalue">Value</label>
                                                <input type="text" name="fieldvalue" id="fieldvalue" class="form-input"
                                                    v-model="tbaFieldvalue">
                                            </div>
                                            <div class="flex flex-col-reverse">
                                                <button type="submit" class="form-button">Add</button>
                                            </div>
                                            <div class="flex flex-col-reverse">
                                                <button type="reset" class="bg-amber-700 form-button"
                                                    @click="userFields = []">Clear</button>
                                            </div>
                                            <div class="flex flex-col-reverse">
                                                <button type="submit" class="bg-emerald-600 form-button"
                                                    @click="uploadManualFields" :disabled="enoughfields">
                                                    Create Quiz
                                                </button>
                                            </div>
                                        </div>
                                    </form>
                                </div>

                            </div>
                            <div v-else class="flex justify-start ml-[5%] mr-auto">
                                <div>
                                    <form @submit.prevent="createDSF" class="flex flex-col" enctype="multipart/form-data">
                                        <label for="DSF" class="text-lg font-bold">Import from file</label>
                                        <input class="rounded-md bg-snytext-lite" type="file" name="DSF" id="DSF" ref="DSF"
                                            placeholder="Text file" @change="handleFileChange">
                                        <input class="form-button w-max m-2 mx-auto" type="submit" value="Submit"
                                            @click="uploadFile">
                                    </form>
                                </div>
                            </div>

                        </div>
                    </form>
                </div>
            </template>
        </fwb-modal>

        <!-- Load-a-quiz-modal -->
        <fwb-modal size="5xl" v-if="loadModal" class="max-w-5xl">
            <template #header>
                <div class="w-full">
                    <h2 class="h2-c">Load a quiz</h2>
                    <button type="button" @click="toggleLoadModal"
                        class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-snytext rounded-lg text-sm w-8 h-8 ml-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white">
                        <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                            viewBox="0 0 14 14">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
                        </svg>
                        <span class="sr-only">Close modal</span>
                    </button>
                </div>
            </template>
            <template #body>
                <div class="flex flex-row w-full">
                    <div class="flex flex-col items-start">
                        <h3 class="h3">Your Quizzes</h3>
                        <ol class="border-2 rounded-md border-gray-300 w-max p-2">
                            <li v-for="quiz in quizzes" :key="quiz"><button
                                    class="bg-gray-400 rounded-md p-2 my-1 font-semibold" @click="dispQuiz(quiz)">{{ quiz
                                    }}</button></li>
                        </ol>
                    </div>
                    <div class="flex flex-col mx-auto">
                        <h3 class="h3">Quiz data</h3>
                        <div v-if="dispQuizData" class="items-end">
                            <ol class="border-2 rounded-md border-gray-300 p-2">
                                <li v-for="pair in dispQuizData" :key="pair">
                                    <span class="font-semibold">Q:</span> {{ pair.Q
                                    }} <span class="font-black mx-4 text-center">:</span>
                                    <span class="font-semibold">A:</span> {{ pair.A }}
                                </li>
                            </ol>
                        </div>
                    </div>
                </div>
            </template>
            <template #footer></template>
        </fwb-modal>

    </main>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { FwbModal } from 'flowbite-vue';
import axios from 'axios';

import { FwbTabs, FwbTab } from 'flowbite-vue';
const activeTab = ref('Typed Answer')

const apiKey = import.meta.env.VITE_API_KEY;
const apiURL = import.meta.env.VITE_API_URL;
const dataset = ref()
const selectedFile = ref()
const datasets = ref(0)
const quizzes = ref<string[]>([])
const loading = ref(true)
const createModal = ref(false)
const loadModal = ref(false)
const quizType = ref('None')
const quizName = ref()
const quizDescription = ref()
const quizSeparator = ref('None')
const dispSeparator = ref()
const csrf = ref()
const userFields = ref<{ Q: string, A: string }[]>([])
const tbaFieldkey = ref()
const tbaFieldvalue = ref()
const errortext = ref()
const enoughfields = ref(false)
const dispQuizData = ref()

function addFields() {
    userFields.value.push({ Q: tbaFieldkey.value, A: tbaFieldvalue.value })
    tbaFieldkey.value = ''
    tbaFieldvalue.value = ''
    console.log(userFields.value)
    if (userFields.value.length >= 4) {
        enoughfields.value = true
    } else {
        enoughfields.value = false
    }
}

async function dispQuiz(quiz: string) {
    console.log(quiz)
    await axios.get(apiURL + '/study/quiz/get', {
        headers: {
            'X-API-KEY': apiKey
        },
        withCredentials: true
    })
        .then(response => {
            console.log(response.data)
            let index = response.data.quizzes.findIndex((obj: { quizName: string; }) => obj.quizName == quiz)
            dispQuizData.value = response.data.quizzes[index].questions

        })
        .catch(error => {
            console.log(error)
        })
}

function changeSeparator() {
    if (quizSeparator.value == 'dash') {
        dispSeparator.value = ' - '
    } if (quizSeparator.value == 'equals') {
        dispSeparator.value = ' = '
    } if (quizSeparator.value == 'colon') {
        dispSeparator.value = ' : '
    } if (quizSeparator.value == 'semicolon') {
        dispSeparator.value = ' ; '
    } if (quizSeparator.value == 'tab') {
        dispSeparator.value = ' → '
    } if (quizSeparator.value == 'None') {
        dispSeparator.value = ' '
    }
}



const manualFields = ref(true)

function toggleCreateModal() {
    createModal.value = !createModal.value
}
function toggleLoadModal() {
    loadModal.value = !loadModal.value
}
function switchButton() {
    manualFields.value = !manualFields.value
}


async function load() {
    await axios.get(apiURL + '/study/quiz/get', {
        headers: {
            'X-API-KEY': apiKey
        },
        withCredentials: true
    })
        .then(response => {
            datasets.value = response.data.quizzes.length
            console.log(response.data)
            console.log(response.data.quizzes.length)
            for (let i = 0; i <= datasets.value - 1; i++) {
                quizzes.value.push(response.data.quizzes[i].quizName)
                console.log(quizzes.value)
            }
        })
        .catch(error => {
            console.log(error)
        })

    await axios.get(`${apiURL}/getCSRF`, {
        headers: {
            'X-API-KEY': apiKey
        },
        withCredentials: true
    })
        .then(response => {
            csrf.value = response.data.csrf
            console.log(response.data)
        })
        .catch(error => {
            console.log(error)
        })

    loading.value = false
}




function createDSF() {
    console.log(dataset.value)
}

const handleFileChange = (event: any) => {
    selectedFile.value = event.target.files[0];
    console.log(selectedFile.value)
};

async function uploadFile() {
    const formData = new FormData();
    formData.append('file', selectedFile.value);
    await axios.post(`${apiURL}/study/quiz/create`, formData, {
        headers: {
            'X-API-KEY': apiKey,
            'Content-Type': 'multipart/form-data',
            "X-CSRF-TOKEN": csrf.value,
            "X-FROM-FILE": "true",
        },
        withCredentials: true
    })
        .then(response => {
            console.log(response.data)
            createModal.value = false
        })
        .catch(error => {
            console.log(error)
            errortext.value = error.response.data.error
        })
}

async function uploadManualFields() {
    await axios.post(`${apiURL}/study/quiz/create`, {
        quizName: quizName.value,
        quizDescription: quizDescription.value,
        quizType: quizType.value,
        quizSeparator: quizSeparator.value,
        quizData: userFields.value
    }, {
        headers: {
            'X-API-KEY': apiKey,
            'Content-Type': 'application/json',
            "X-CSRF-TOKEN": csrf.value,
            "X-FROM-FILE": "false",
        },
        withCredentials: true
    })
        .then(response => {
            console.log(response.data)
            createModal.value = false
        })
        .catch(error => {
            console.log(error)
            errortext.value = error.response.data.error
        })
}






load()


</script>

<style lang="scss" scoped></style>
