<template>
    <main>
        <h1 class="h1">Logging you out...</h1>
    </main>
</template>

<script setup lang="ts">
import axios from 'axios';
import { useRouter } from 'vue-router'

const router = useRouter()

const apiKey = import.meta.env.VITE_API_KEY
const apiURL = import.meta.env.VITE_API_URL

async function logOut() {
    await axios.delete(`${apiURL}/logout`,
        {
            headers: {
                "X-API-KEY": apiKey,
            },
            withCredentials: true,
        }
    ).then((response) => {
        if (response.status == 200) {
            window.location.reload()
            router.push('/')
        }
    }).catch((error) => {
        console.log(error)
    })
}

logOut()
</script>