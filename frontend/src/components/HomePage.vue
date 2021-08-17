<template>
  <div class="container">
    <div class="px-4 py-5 border shadow-lg">
      <h1 class="display-5 fw-bold">
        Values and Principles of Agile Software Development
      </h1>
      <div class="btn-group">
        <button
          type="button"
          class="pb-2 btn btn-outline-primary"
          data-bs-toggle="modal"
          data-bs-target="#values"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-plus-square-fill"
            viewBox="0 0 16 16"
          >
            <path
              d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm6.5 4.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3a.5.5 0 0 1 1 0z"
            />
          </svg>
          Add Value
        </button>
        <AddModal
          type="values"
          :listReload="listReload"
          @submitForm="listReload++"
        />
        <button
          type="button"
          class="pb-2 btn btn-outline-primary"
          data-bs-toggle="modal"
          data-bs-target="#principles"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-plus-square-fill"
            viewBox="0 0 16 16"
          >
            <path
              d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm6.5 4.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3a.5.5 0 0 1 1 0z"
            />
          </svg>
          Add Principle
        </button>
        <AddModal
          type="principles"
          :listReload="listReload"
          @submitForm="listReload++"
        />
      </div>
      <div class="container px-4 py-5" id="featured-3">
        <div class="row">
          <h2 class="pb-2 border-bottom">Values</h2>
        </div>
        <List :key="listReload" @updateEntry="listReload++" type="values" />
        <div class="row">
          <h2 class="pb-2 border-bottom">Principles</h2>
        </div>
        <List :key="listReload" @updateEntry="listReload++" type="principles" />
      </div>
    </div>
    <div class="b-example-divider"></div>
  </div>
</template>

<script>
import List from "@/components/List.vue";
import AddModal from "@/components/AddModal.vue";

export default {
  components: {
    List,
    AddModal,
  },
  data() {
    return {
      listReload: 0,
    };
  },
};
</script>
