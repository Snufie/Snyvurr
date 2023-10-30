<template>
    <main>
        <div class="my-7 px-7 [&>*:nth-child(odd)]:h3-r [&>*:nth-child(odd)]:flex-vcenter griddy">
            <div class="col-span-1">Functions</div>
            <div class="bg-green-400 flex">
                <RouterLink to="/functions/studytools" class="bg-vida-loca-200 hover:bg-vida-loca-600 form-button">
                    StudyTools
                </RouterLink>
                <RouterLink to="/functions/calendar" class="bg-vida-loca-200 hover:bg-vida-loca-600 form-button">
                    Calendar
                </RouterLink>
            </div>
        </div>
    </main>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<style lang="scss" scoped>
.griddy {
    display: grid;
    grid-template-columns: minmax(7rem, 25%) 1fr;
    column-gap: 1%;

    &>* {
        height: 100%;
        padding: 1rem;
    }

    &> :nth-child(odd) {
        background-color: theme('colors.vida-loca[200]');
        font-weight: bold;
        border-radius: theme('borderRadius.md') 0 0 theme('borderRadius.md');
    }

    &>:nth-child(even) {
        border-radius: 0 theme('borderRadius.md') theme('borderRadius.md') 0;

        &>a {
            margin-left: 2%;
        }
    }

}
</style>