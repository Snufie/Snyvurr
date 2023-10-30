<template>
    <main>
        <div class="text-center w-full my-4">
            <h1 class="h1">Welcome to SnyChat!</h1>
            <p>
                It looks like it is your first time here so let's set up your account.
            </p>
        </div>
        <div class="py-2 px-4 mx-auto max-w-screen-xl sm:py-6 lg:px-6">
            <div class="space-y-8 md:grid gridclass align-bottom self-center  md:space-y-0">
                <div class="flex flex-wrap justify-center items-center text-center mb-4 w-fit h-min rounded-full">
                    <h2 class="h2 tracking-tight ">What is SnyChat?</h2>
                    <p class="mt-2 text-zinc-500 font-medium">
                        SnyChat is a real-time chat application that allows you to chat with other users of the Network.
                    </p>
                </div>
                <hr class="border-4 rounded-full m-auto w-3 h-3 border-vida-loca-100 bg-vida-loca-100 self-center">
                <div class=" flex flex-wrap justify-center items-center text-center mb-4 w-fit h-min rounded-full">
                    <h2 class="h2 tracking-tight ">Why use SnyChat?</h2>
                    <p class="mt-2 text-zinc-500 font-medium">
                        SnyChat serves as a technical demonstration of the Snyvurr Network's capabilities. It is also a
                        great way to connect with other users of the Network.
                    </p>
                </div>
                <hr class="border-4 rounded-full m-auto w-3 h-3 border-vida-loca-100 bg-vida-loca-100 self-center">
                <div class="flex flex-wrap justify-center items-center text-center mb-4 w-fit h-min rounded-full">
                    <h2 class="h2 tracking-tight ">Is it secure?</h2>
                    <p class="mt-2 text-zinc-500 font-medium">
                        Yes, SnyChat is secure. All messages are encrypted using the Snyvurr Network's encryption protocol.
                        If you feel unsafe or fear for the safety of others, please contact the Snyvurr Network's admin.
                    </p>
                </div>
            </div>
        </div>
        <hr class="border-vida-loca-200 border mx-4 rounded-full my-4">
        <div class="text-center items-center justify-center flex flex-wrap flex-col">
            <h1 class="h1 my-2">Rules:</h1>
            <p class="mb-2">
                Please follow these rules when using SnyChat:
            <ol class="list-disc text-left mx-auto">
                <li>Be respectful of others.</li>
                <li>Do not spam.</li>
                <li>Do not post NSFW content.</li>
                <li>Do not post illegal content.</li>
                <li>Do not post content that violates the Snyvurr Network's Terms of Service.</li>
            </ol>
            Breaking these rules may result in your account being removed from the Snyvurr Network as a whole.
            </p>
            <button @click="InitChatAcc" type="button"
                class="px-4 py-2 text-vida-loca-25 bg-vida-loca-400 rounded-md my-2 mx-auto">I accept the rules</button>
        </div>

        <fwb-modal size="2xl" v-if="createAcc" class="max-w-2xl">
            <template #header>
                <div class="text-center w-full">
                    <h1 class="h1 font-bold">Create SnyChat profile</h1>
                </div>
            </template>
            <template #body>
                <div class="w-full">
                    <form @submit.prevent="createChatProfile" class="flex flex-col">
                        <div>
                            <label for="ChatName">Username</label>
                            <input v-model="chatName" type="text" id="ChatName" name="ChatName" required
                                class="rounded-md my-2 mx-auto">
                        </div>
                    </form>
                </div>
            </template>
        </fwb-modal>
    </main>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { FwbModal } from 'flowbite-vue'


const chatName = ref('')
const createAcc = ref(false)

function InitChatAcc() {
    createAcc.value = true
}
async function createChatProfile() {
    return
}
</script>

<style lang="scss" scoped>
.gridclass {
    grid-template-columns: repeat(5, 1fr, 6rem);
    gap: 2rem;
    justify-content: center;

    :nth-child(1) {
        grid-column: 1 / 1;
    }

    :nth-child(2) {
        grid-column: 2/2;
    }

    :nth-child(3) {
        grid-column: 3/3;
    }

    :nth-child(4) {
        grid-column: 4/4;
    }

    :nth-child(5) {
        grid-column: 5/5;
    }
}
</style>