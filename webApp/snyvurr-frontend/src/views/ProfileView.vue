<template>
    <div class="profile">
        <h1>This is an about page</h1>
    </div>
</template>

<script setup>
import router from '../router';
import axios from 'axios';

usertoken = localStorage.getItem('token')
if (usertoken == null || usertoken == undefined) {
    router.push('/')
}

async function getUser() {
    try {
        const response = await axios.get('/getUser?user=' + usertoken)
        if (response.status == 200) {
            console.log(response.data)
        }
    } catch (error) {

    }


}
</script>

<script>
import axios from 'axios';
import { ref } from 'vue';

export default {
    data() {
        return {

        }
    },
    methods: {
        logout() {
            localStorage.removeItem('token')
            router.push('/')
        }
    }
}
</script>

<style>
@media (min-width: 1024px) {
    .about {
        min-height: 100vh;
        display: flex;
        align-items: center;
    }
}
</style>