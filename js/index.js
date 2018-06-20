import { formats } from "./format.js";
import { duplicates } from "./duplicate.js";
import { branches } from "./branch.js";
import { dirs } from "./dir.js";
import { words } from "./word.js";
import { times } from "./time.js";

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
});

let branch = new Vue({
  el: "#branch",
  data: {
    branches: branches
  }
});

let dir = new Vue({
  el: "#dir",
  data: {
    dirs: dirs
  }
});

let word = new Vue({
  el: "#word",
  data: {
    words: words
  }
});

let time = new Vue({
  el: "#time",
  data: {
    times: times
  }
});
