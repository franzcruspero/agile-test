<template>
  <div class="container">
    <h1 class="visually-hidden">Heroes examples</h1>

    <div class="px-4 py-5 border shadow-lg">
      <h1 class="display-5 fw-bold">
        Values and Principles of Agile Software Development
      </h1>
      <div class="row">
        <button
          type="button"
          class="pb-2 btn btn-primary"
          data-bs-toggle="modal"
          data-bs-target="#values"
        >
          Add Value
        </button>
        <AddModal
          type="values"
          :list_reload="list_reload"
          @submitForm="list_reload++"
        />
        <button
          type="button"
          class="pb-2 btn btn-primary"
          data-bs-toggle="modal"
          data-bs-target="#principles"
        >
          Add Principle
        </button>
      </div>
      <AddModal
        type="principles"
        :list_reload="list_reload"
        @submitForm="list_reload++"
      />
      <div class="container px-4 py-5" id="featured-3">
        <div class="row">
          <h2 class="pb-2 border-bottom">Values</h2>
        </div>
        <List :key="list_reload" @submitForm="list_reload++" type="values" />
        <div class="row">
          <h2 class="pb-2 border-bottom">Principles</h2>
        </div>
        <List :key="list_reload" type="principles" />
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
      name: "",
      description: "",
      list_reload: 0,
    };
  },
};
</script>
