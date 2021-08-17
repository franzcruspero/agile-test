<template>
  <div>
    <div
      class="modal fade"
      id="update"
      tabindex="-1"
      aria-labelledby="label"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="label">
              Update Value/Principle {{ type }} {{ this.id }}
            </h5>
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
                <label for="name" class="form-label">Name</label>
                <input
                  type="text"
                  class="form-control"
                  id="name"
                  placeholder=""
                  v-model="currentName"
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
                  v-model="currentDescription"
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
    id: Number,
    name: String,
    description: String,
  },
  data() {
    return {
      currentName: this.name,
      currentDescription: this.description,
    };
  },
  methods: {
    async submitForm() {
      await axios.patch(
        `http://localhost:8000/api/v1/${this.type}/${this.id}/`,
        {
          name: this.currentName,
          description: this.currentDescription,
        }
      );
      this.$emit("submitForm");
    },
  },
};
</script>
