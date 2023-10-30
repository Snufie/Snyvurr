<template>
    <main>
        <div v-if="!loading" class="profile">
            <div class="flex flex-wrap flex-col h-fit ml-4 self-start align-top">
                <h1 class="text-5xl font-black tracking-tight leading-snug text-left">Hey, {{ user.username }}!</h1>
                <h2 class="ml-4 text-xl font-medium tracking-tight leading-4 text-left">Welcome to your profile page.</h2>
            </div>
            <section class="rounded-md mt-6 p-6 ml-6 w-2/3 bg-gradient-to-br from-green-200 to-gray-50">
                <div v-if="!IsEditing">
                    <h1 class="text-5xl font-bold tracking-tight">{{ user.username }}</h1>
                    <div class="flex flex-col justify-end w-fit ml-96 shadow-sm shadow-neutral-500 rounded-lg p-5">
                        <div class="mb-1">
                            <label for="dispEmail" class="font-bold">Your E-mail:</label>
                            <span class="ml-2" id="dispEmail">{{ user.email
                            }}</span> <i v-if="user.verifiedmail" class="fa-solid fa-circle-check ml-1"></i>
                        </div>
                        <div class="mb-1">
                            <label for="dispUname" class="font-bold">Your username:</label>
                            <span class="ml-2" id="dispEmail">{{ user.username
                            }}</span>
                        </div>
                        <div class="mb-1">
                            <label for="dispPhone" class="font-bold">Your phone number:</label>
                            <span v-if="user.phone" class="ml-2" id="dispPhone">{{ user.phone }}</span>
                            <span v-else class="ml-2 text-gray-500" id="dispPhone">No phone number</span>
                            <i v-if="user.verifiedphone" class="fa-solid fa-circle-check ml-1"></i>
                        </div>
                        <div class="mb-1">
                            <label for="dispRole" class="font-bold">Your role:</label>
                            <span class="ml-2" id="dispRole">{{ user.role }}</span>
                        </div>
                        <a @click="IsEditing = !IsEditing"
                            class="font-semibold text-emerald-700 hover:text-dark hover:underline">
                            Edit Profile
                        </a>
                    </div>
                </div>
                <div v-else>
                    <h1 class="text-5xl font-bold tracking-tight">{{ user.username }}</h1>
                    <form @submit.prevent="editProfile"
                        class="flex flex-wrzap flex-col justify-end w-fit ml-96 shadow-sm shadow-neutral-500 rounded-lg p-5">
                        <label for="dispEmail">Edit E-mail:</label>
                        <input id="dispEmail" type="email" v-model="newEmail" placeholder="New E-mail">
                        <label for="dispPhone">Edit Phone Number:</label>
                        <input id="dispPhone" type="tel" v-model="newPhone" placeholder="New Phone Number">
                        <label for="dispUname">Edit Username:</label>
                        <input id="dispUname" type="text" v-model="newUname" placeholder="New Username">
                        <div class="flex flex-wrap flex-row justify-center">
                            <button type="submit"
                                class="rounded-md m-2 w-max p-2 px-3  font-semibold bg-lime-600 text-snytext-lite hover:text-green-300 hover:bg-lime-800">
                                Save Changes</button>
                            <button @click="IsEditing = !IsEditing"
                                class="rounded-md m-2 w-max p-2 px-3  font-semibold bg-emerald-600 text-white hover:text-green-300 hover:bg-hover">
                                Cancel</button>
                        </div>
                    </form>
                </div>
            </section>
            <section class="rounded-md mt-6 p-6 ml-6 w-2/3 bg-red-50">
                <div>
                    <h1 class="h1 text-red-900">Danger Zone</h1>
                    <hr class="border-red-950">
                    <div class=" p-2">
                        <h2 class="h2">Delete Account</h2>
                        <p>This deletes your account and all stored and/or cached data alongside it.</p>
                        <button @click="openConfirmDelModal"
                            class="rounded-md bg-red-600 text-white px-2 py-1 mt-1 ml-3">Delete
                            Account</button>
                    </div>
                </div>
                <fwb-modal size="lg" v-if="confirmDelModalOpen" class="max-w-lg">
                    <template #header>
                        <h1 class="h1 text-center w-full">Confirm Deletion</h1>
                        <hr>
                    </template>
                    <template #body>
                        <div class="flex flex-col">
                            <p class="w-full">
                                Are you sure your want to delete your account? This action deletes all traces of your
                                account
                                and all data associated with it. This action cannot be undone.
                            </p>
                            <p class="mt-3 text-center font-bold text-lg">
                                Type your password to confirm.
                            <form @submit.prevent="delAccount" class="flex flex-col h-fit mx-auto mt-2">
                                <input type="password" v-model="confirmDelPsw" id="confirmDelPsw"
                                    class="rounded-md max-h-8">
                                <div class="flex flex-row justify-evenly w-full space-y-2">
                                    <button type="submit"
                                        class="rounded bg-red-600 font-bold text-white px-3 py-2 mt-2">Delete
                                        Account</button>
                                    <button @click="closeConfirmDelModal" type="button"
                                        class="rounded bg-emerald-200 font-bold text-snytext px-3 py-2">Cancel</button>
                                </div>
                            </form>
                            </p>
                        </div>
                    </template>
                </fwb-modal>
            </section>
        </div>
        <div v-else>
            <span class="loader"></span>
        </div>
    </main>
</template>

<script setup lang="ts">
import { ref } from 'vue';

import { FwbModal } from 'flowbite-vue'

const IsEditing = ref(false)

import axios from 'axios';
const apiKey = import.meta.env.VITE_API_KEY
const apiURL = import.meta.env.VITE_API_URL
const user = ref({ username: '', email: '', verifiedmail: false, phone: '', verifiedphone: false, role: '' })
const newEmail = ref('')
const newPhone = ref('')
const newUname = ref('')

const confirmDelModalOpen = ref(false)
const confirmDelPsw = ref('')
const loading = ref(true)
const CSRF = ref()


async function getProfile() {

    await axios.get(`${apiURL}/getUser`,
        {
            headers: {
                "X-API-KEY": apiKey,
            },
            withCredentials: true,
        }).then((response) => {
            user.value = response.data
            console.log(user.value)
        }).catch((error) => {
            console.log(error)
        })
}

async function load() {
    await getProfile()
    loading.value = false
}

function openConfirmDelModal() {
    confirmDelModalOpen.value = true
}
function closeConfirmDelModal() {
    confirmDelModalOpen.value = false
}

async function editProfile() {
    loading.value = true
    if (newEmail.value == "") {
        newEmail.value = user.value.email
    }
    if (newPhone.value == "") {
        newPhone.value = user.value.phone
    }
    if (newUname.value == "") {
        newUname.value = user.value.username
    }
    await axios.get(`${apiURL}/getCSRF`, {
        headers: {
            "X-API-KEY": apiKey,
        },
        withCredentials: true,
    }).then((response) => {
        console.log(response)
        CSRF.value = response.data.csrf
    }).catch((error) => {
        console.log(error)
    })
    await axios.post(`${apiURL}/editUser`, {
        email: newEmail.value,
        phone: newPhone.value,
        username: newUname.value
    },
        {
            headers: {
                "X-API-KEY": apiKey,
                "X-CSRF-TOKEN": CSRF.value,
            },
            withCredentials: true,
        }).then((response) => {
            console.log(response)
            IsEditing.value = false
            loading.value = false
            window.location.reload()
        }).catch((error) => {
            console.log(error)
        })
}

async function delAccount() {

}

load()
</script>



<style lang="scss" scoped></style>