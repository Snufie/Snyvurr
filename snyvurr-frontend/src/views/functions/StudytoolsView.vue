<template>
    <main>
        <div class="m-7 grid grid-cols-3">
            <RouterLink class="form-button w-full" to="/functions/studytools/flashcards">
                Flashcards
            </RouterLink>
            <RouterLink class="form-button w-full" to="/functions/studytools/quiz">
                Quiz
            </RouterLink>
            <RouterLink class="form-button w-full" to="/functions/studytools/eznotes">
                EZ Notes
            </RouterLink>
        </div>
    </main>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>