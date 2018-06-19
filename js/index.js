import {
    formats
} from "./js/format.js"
import {
    duplicates
} from "./js/duplicate.js"
import {
    branches
} from "./js/branch.js"
import {
    times
} from "./js/time.js"

let format = new Vue({
    el: "#format",
    data: {
        formats: formats
    }
});

let duplicate = new Vue({
    el: "#duplicate",
    data: {
        duplicates: duplicates
    }
})

let branch = new Vue({
    el: "#branch",
    data: {
        branches: branches
    }
})

let time = new Vue({
    el: "#time",
    data: {
        times: times
    }
})
