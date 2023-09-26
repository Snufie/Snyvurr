<template>
  <main>
    <div class="py-4 pl-4">
      <h1 class="text-5xl font-black tracking-tight leading-snug text-center">Welcome to Snyvurr Network</h1>
      <img class="w-3/6 h-3/6 mx-auto" src="../assets/construction_site.svg" alt="under construction">
      <p class="bg-vida-loca-50 w-11/12 text-center px-4 py-2 rounded-md mx-auto">
        This is the home page.
        <br>
        This page is under development, and you shouldn't be able to see this.
      </p>
    </div>
    <hr class="bg-vida-loca-600 mx-4 h-0.5 rounded-md">
    <div class="pl-4">

      <section class="bg-white dark:bg-gray-900">
        <div class="py-8 px-4 mx-auto max-w-screen-xl text-center lg:py-16">
          <h1
            class="mb-4 text-4xl font-extrabold tracking-tight leading-none text-snytext md:text-5xl lg:text-6xl dark:text-white">
            A platform for nerds, by nerds</h1>
          <p class="mb-8 text-lg font-normal text-gray-500 lg:text-xl sm:px-16 lg:px-48 dark:text-gray-400">
            Snyvurr is like a digital pocket knife, utilities galore! Whether you find them useful or not,
            Snyvurr serves as a playground for us to learn and grow as developers, and as a service for you
            to use and learn about too.
          </p>
          <div class="flex flex-col space-y-4 sm:flex-row sm:justify-center sm:space-y-0 sm:space-x-4">
            <button data-modal-target="login-modal" data-modal-show="login-modal"
              class="inline-flex justify-center items-center py-3 px-5 text-base font-medium text-center text-white rounded-lg bg-vida-loca-500 hover:transition-colors hover:bg-vida-loca-600 focus:ring-4 focus:ring-emerald-300 dark:focus:ring-emerald-900">
              Get started
              <svg class="w-3.5 h-3.5 ml-2 text-vida-loca-25" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                fill="none" viewBox="0 0 14 10">
                <path stroke="white" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M1 5h12m0 0L9 1m4 4L9 9" />
              </svg>
            </button>
            <RouterLink to="/about"
              class="inline-flex justify-center items-center py-3 px-5 text-base font-medium text-center text-snytext rounded-lg border border-gray-300 hover:transition-colors hover:bg-gray-100 focus:ring-4 focus:ring-gray-100 dark:text-white dark:border-gray-700 dark:hover:bg-gray-700 dark:focus:ring-gray-800">
              Learn more</RouterLink>
          </div>
        </div>
      </section>

    </div>

    <!-- Login modal -->
    <div id="login-modal" tabindex="-1" aria-hidden="true"
      class="fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full">
      <div class="relative w-full max-w-md max-h-full">
        <!-- Modal content -->
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
          <button type="button"
            class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-snytext rounded-lg text-sm w-8 h-8 ml-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
            data-modal-hide="login-modal">
            <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
            </svg>
            <span class="sr-only">Close modal</span>
          </button>
          <div class="px-6 py-6 lg:px-8">
            <h3 class="mb-4 text-xl font-medium text-snytext dark:text-white">Login</h3>
            <form class="space-y-6" @submit.prevent="login">
              <div>
                <label for="email" class="block mb-2 text-sm font-medium text-snytext dark:text-white">Your
                  email</label>
                <input type="email" v-model="Email" id="email"
                  class="bg-gray-50 border border-gray-300 text-snytext text-sm rounded-lg focus:ring-emerald-500 focus:border-emerald-500 block w-full p-2.5"
                  placeholder="example@mail.com" required>
              </div>
              <div>
                <div class="flex flex-row justify-between">
                  <label for="password" class="flex mb-2 text-sm font-medium text-snytext dark:text-white">Your
                    password</label>
                  <div class="flex justify-right">
                    <a href="#" class="text-sm text-emerald-700 hover:underline dark:text-emerald-500">Forgot
                      Password?</a>
                  </div>
                </div>
                <input type="password" v-model="Password" id="password" placeholder="••••••••"
                  class="bg-gray-50 border border-gray-300 text-snytext text-sm rounded-lg focus:ring-emerald-500 focus:border-emerald-500 block w-full p-2.5"
                  required>
              </div>
              <button type="submit" data-modal-hide="login-modal"
                class="w-full text-white bg-vida-loca-500 hover:bg-vida-loca-700 focus:ring-4 focus:outline-none focus:ring-emerald-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-emerald-600 dark:hover:bg-emerald-700 dark:focus:ring-emerald-800">Login
                to your account</button>
              <div class="text-sm font-medium text-gray-500 dark:text-gray-300">
                Don't have an account? <a data-modal-target="register-modal" data-modal-hide="login-modal"
                  data-modal-show="register-modal"
                  class="text-emerald-700 hover:underline dark:text-emerald-500 cursor-pointer">Create
                  one</a>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>


    <!-- Register modal -->
    <div id="register-modal" tabindex="-1" aria-hidden="true"
      class="fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full">
      <div class="relative w-full max-w-md max-h-full">
        <!-- Modal content -->
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
          <button type="button"
            class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-snytext rounded-lg text-sm w-8 h-8 ml-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
            data-modal-hide="register-modal">
            <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
            </svg>
            <span class="sr-only">Close modal</span>
          </button>
          <div class="px-6 py-6 lg:px-8">
            <h3 class="mb-4 text-xl font-medium text-snytext dark:text-white">Register</h3>
            <form class="space-y-6" @submit.prevent="register">
              <div>
                <label for="email" class="block mb-2 text-sm font-medium text-snytext dark:text-white">Your
                  email</label>
                <input type="email" v-model="Email" id="email"
                  class="bg-gray-50 border border-gray-300 text-snytext text-sm rounded-lg focus:ring-emerald-500 focus:border-emerald-500 block w-full p-2.5"
                  placeholder="example@mail.com" required>
              </div>
              <div>
                <div class="flex flex-row justify-between">
                  <label for="password" class="flex mb-2 text-sm font-medium text-snytext dark:text-white">Your
                    password</label>
                </div>
                <input type="password" v-model="Password" id="password" placeholder="••••••••"
                  class="bg-gray-50 border border-gray-300 text-snytext text-sm rounded-lg focus:ring-emerald-500 focus:border-emerald-500 block w-full p-2.5"
                  required>
              </div>
              <div>
                <label for="Cpassword" class="flex mb-2 text-sm font-medium text-snytext dark:text-white">
                  Confirm password</label>
                <input type="password" @input="checkPsw" v-model="ConfirmPassword" id="Cpassword" placeholder="••••••••"
                  class="bg-gray-50 border border-gray-300 text-snytext text-sm rounded-lg focus:ring-emerald-500 focus:border-emerald-500 block w-full p-2.5"
                  required>
                <label v-if="PswNoMatch" class="mb-2 text-sm font-medium text-red-600">Passwords don't match!</label>
              </div>
              <button type="submit" v-bind:disabled="!PswNoMatch"
                class="w-full text-white bg-vida-loca-500 hover:bg-vida-loca-700 focus:ring-4 focus:outline-none focus:ring-emerald-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-emerald-600 dark:hover:bg-emerald-700 dark:focus:ring-emerald-800">
                Create your account</button>
              <div class="text-sm font-medium text-gray-500 dark:text-gray-300">
                Already have an account? <a data-modal-hide="register-modal" data-modal-toggle="login-modal"
                  data-modal-target="login-modal"
                  class="text-emerald-700 hover:underline dark:text-emerald-500 cursor-pointer">Log
                  in</a>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import axios from 'axios'
import { RouterLink } from 'vue-router';
import { Buffer, btoa } from 'buffer'


const API_KEY = import.meta.env.VITE_API_KEY



export default {
  name: 'HomeView',
  data() {
    return {
      Email: '',
      Password: '',
      ConfirmPassword: '',
      PswNoMatch: false,
      isTyping: false,
      apiKey: API_KEY
    }
  },
  methods: {
    async login() {
      try {
        const encoder = new TextEncoder()
        const data = encoder.encode(`${this.Email}:${this.Password}`)
        const authCred = Buffer(String.fromCharCode.apply(null, data))
        const response = await axios.post('https://api-snyvurr.onrender.com/login', {
          email: this.Email,
          password: this.Password
        }, {
          headers: {
            "X-API_KEY": this.apiKey,
            Authorization: "Basic " + authCred
          }
        }
        );

        if (response.status == 200) {
          localStorage.setItem('token', response.data.token)
          this.$router.push('/profile')
        }
      } catch (error) {
        console.log("An error occurred:", error)
      }
    },
    async register() {
      try {
        const response = await axios.post('https://api-snyvurr.onrender.com/register', {
          headers: {
            "X-API_KEY": API_KEY
          },
          email: this.Email,
          user: this.User,
          password: this.Password,
          confirm_password: this.ConfirmPassword
        });


      } catch (error) {
        console.log("An error occurred:", error)
      }
    },
    async checkPsw() {
      if (this.Password != this.ConfirmPassword) {
        this.PswNoMatch = true
      } else {
        this.PswNoMatch = false
      }
    }
  }
}

</script>

<style lang="scss" scoped></style>
