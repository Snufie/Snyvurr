<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'

import { authenticated } from './router/index'
import { ref } from 'vue'

// const apiKey = import.meta.env.VITE_API_KEY
// const apiURL = import.meta.env.VITE_API_URL
const auth = ref(authenticated)


</script>

<template>
  <header v-if="!auth">
    <div class="navbar overflow-hidden flex content-center dark:bg-vida-loca-800 dark:text-vida-loca-25">
      <h1 class="h1 self-center ml-4">Snyvurr Network</h1>
      <div class="mx-auto">
        <RouterLink :key="$route.fullPath"
          class="text-2xl hover:text-snytext-lite hover:duration-300 hover:transition-colors font-bold" to="/">
          Home
        </RouterLink>
        <RouterLink class="text-2xl hover:text-snytext-lite hover:duration-300 hover:transition-colors font-bold"
          to="/about">
          About
        </RouterLink>
      </div>
    </div>
  </header>
  <header v-else>
    <div class="navbar overflow-hidden flex content-center dark:bg-vida-loca-800 dark:text-vida-loca-25">
      <h1 class="h1 self-center ml-4">Snyvurr Network</h1>
      <div class="mx-auto">
        <RouterLink :key="$route.fullPath"
          class="text-2xl hover:text-snytext-lite hover:duration-300 hover:transition-colors font-bold" to="/">
          Home
        </RouterLink>
        <RouterLink class="text-2xl hover:text-snytext-lite hover:duration-300 hover:transition-colors font-bold"
          to="/profile">
          Profile
        </RouterLink>
        <RouterLink class="text-2xl hover:text-snytext-lite hover:duration-300 hover:transition-colors font-bold"
          to="/social">
          Connect
        </RouterLink>
        <RouterLink class="text-2xl hover:text-snytext-lite hover:duration-300 hover:transition-colors font-bold"
          to="/functions">Utilities
        </RouterLink>
      </div>
    </div>
  </header>

  <RouterView />


  <footer class="bg-slate-50 rounded-lg shadow m-4 dark:bg-gray-800">
    <div class="w-full mx-auto max-w-screen-xl p-4 md:flex md:items-center md:justify-between">
      <span class="text-sm text-gray-500 sm:text-center dark:text-gray-400">© 2023 <RouterLink to="/"
          class="hover:underline">Snyvurr™</RouterLink>. All Rights Reserved.
      </span>
      <ul class="flex flex-wrap items-center mt-3 text-sm font-medium text-gray-500 dark:text-gray-400 sm:mt-0">
        <li>
          <RouterLink to="/about" class="mr-4 hover:underline md:mr-6 ">About</RouterLink>
        </li>
        <li>
          <RouterLink to="/privacy-policy" class="mr-4 hover:underline md:mr-6">Privacy Policy</RouterLink>
        </li>
        <li>
          <RouterLink to="/contact" class="mr-4 md:mr-6 hover:underline">Contact</RouterLink>
        </li>
        <li v-if="auth">
          <RouterLink to="/logout" class="hover:underline">Logout</RouterLink>
        </li>
      </ul>
    </div>
  </footer>
</template>

<style lang="scss">
:root {
  --primary: #4ac679;
  --primary-alt: #1b9b56;
  --light: #d1ffe7;
  --dark: #213731;
  --text: #05242e;
  --text-light: #eafff6;
  --text-hover: #3e54d5;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  color: var(--text);
}



.navbar {
  background-color: var(--primary);
  color: var(--text);
  display: flex;

  a {
    float: left;
    padding: 1rem 2rem;
  }
}

header a:hover {
  transition: background-color 0.2s ease-in-out;
  background-color: var(--primary-alt);
}

header a.router-link-exact-active {
  color: var(--text-light);
  background-color: var(--primary-alt);
}
</style>
