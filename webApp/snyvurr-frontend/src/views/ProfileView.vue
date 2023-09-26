<template>
    <div class="profile">
        <div class="flex flex-wrap flex-col h-fit ml-4 self-start align-top">
            <h1 class="text-5xl font-black tracking-tight leading-snug text-left">Hey, {{ User.username }}!</h1>
            <h2 class="ml-4 text-xl font-medium tracking-tight leading-4 text-left">Welcome to your profile page.</h2>
        </div>

        <section class="rounded-md mt-6 p-6 ml-6 w-2/3 bg-gradient-to-br from-green-200 to-gray-50">
            <div v-if="!IsEditing">
                <h1 class="text-5xl font-bold tracking-tight">{{ User.username }}</h1>

                <div class="flex flex-wrzap flex-col justify-end w-fit ml-96 shadow-sm shadow-neutral-500 rounded-lg p-5">
                    <label for="dispEmail">Your E-mail:</label>
                    <span id="dispEmail">{{ User.email }}</span>
                    <a @click="IsEditing = !IsEditing"
                        class="font-semibold text-emerald-700 hover:text-dark hover:underline">
                        Edit Profile
                    </a>
                </div>
            </div>
            <div v-else>
                <h1 class="text-5xl font-bold tracking-tight">{{ User.username }}</h1>

                <form @submit.prevent="EditProfile()"
                    class="flex flex-wrzap flex-col justify-end w-fit ml-96 shadow-sm shadow-neutral-500 rounded-lg p-5">
                    <label for="dispEmail">Edit E-mail:</label>
                    <input id="dispEmail" type="email" v-model="newEmail" placeholder="New E-mail">
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
    </div>
</template>

<script setup>
import { ref } from 'vue'
const IsEditing = ref(false)
</script>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            User: ''
        }
    },
    methods: {
        async getProfile() {
            const token = localStorage.getItem('token')
            const config = {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
            try {
                const res = await axios.get('https://api-snyvurr.onrender.com/getUser', config)
                console.log(res.data)
                this.User = res.data
                return this.User
            }
            catch (err) {
                console.log('An error occured: ' + err)
            }
        }
    },
    mounted() {
        this.getProfile()
    }
}
</script>



<style lang="scss" scoped></style>