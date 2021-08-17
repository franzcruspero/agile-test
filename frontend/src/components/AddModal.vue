<template>
  <div>
    <div
      class="modal fade"
      :id="type"
      tabindex="-1"
      aria-labelledby="label"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="label">Add Value/Principle</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <form
            @submit.prevent="submitForm"
            class="needs-validation"
            novalidate
          >
            <div class="modal-body">
              <div>
                <label for="title" class="form-label">Title</label>
                <input
                  type="text"
                  class="form-control"
                  id="title"
                  placeholder=""
                  v-model="title"
                  required
                />
                <div class="invalid-feedback">
                  Valid first name is required.
                </div>
              </div>
              <div>
                <label for="description" class="form-label">Description</label>
                <textarea
                  type="text"
                  class="form-control"
                  id="description"
                  placeholder=""
                  v-model="description"
                  rows="3"
                  required
                />
                <div class="invalid-feedback">
                  Valid first name is required.
                </div>
              </div>
            </div>
            <div class="modal-footer">
              <button
                type="button"
                class="btn btn-secondary"
                data-bs-dismiss="modal"
              >
                Close
              </button>
              <button
                type="submit"
                class="btn btn-primary"
                data-bs-dismiss="modal"
              >
                Save changes
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    type: String,
    list_reload: Number,
  },
  data() {
    return {};
  },
  methods: {
    async submitForm() {
      await axios.post(`http://localhost:8000/api/v1/${this.type}/`, {
        title: this.title,
        description: this.description,
      });

      this.title = "";
      this.description = "";
      this.$emit("submitForm");
    },
  },
};
</script>
