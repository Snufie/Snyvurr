<template>
    <div class="profile">
        <div class="flex flex-wrap flex-col h-fit ml-4 self-start align-top">
            <h1 class="text-5xl font-black tracking-tight leading-snug text-left">Hey, {{ User }}!</h1>
            <h2 class="ml-4 text-xl font-medium tracking-tight leading-4 text-left">Welcome to your profile page.</h2>
        </div>

        <section class="rounded-md mt-6 p-6 ml-6 w-2/3 bg-gradient-to-br from-green-200 to-gray-50">
            <div>
                <h1 class="text-5xl font-bold tracking-tight">{{ User }}</h1>

            </div>
        </section>
    </div>
</template>

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
                const res = await axios.get('http://api-snyvurr.onrender.com/getUser', config)
                console.log(res.data)
                this.User = res.data
            }
            catch (err) {
                console.log('An error occured: ' + err)
            }
        }
    }
}
</script>

<style lang="scss" scoped></style>