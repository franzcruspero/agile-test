<template>
  <div>
    <div class="row g-4 py-5 row-cols-1 row-cols-lg-1">
      <ul v-for="(result, index) in results" :key="result.id">
        <div class="col d-flex align-items-start">
          <div class="icon-square bg-light text-dark flex-shrink-0 me-3">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="32"
              height="32"
              fill="currentColor"
              class="bi bi-card-list"
              viewBox="0 0 16 16"
            >
              <path
                d="M14.5 3a.5.5 0 0 1 .5.5v9a.5.5 0 0 1-.5.5h-13a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h13zm-13-1A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h13a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 14.5 2h-13z"
              />
              <path
                d="M5 8a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7A.5.5 0 0 1 5 8zm0-2.5a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5zm0 5a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5zm-1-5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0zM4 8a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0zm0 2.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0z"
              />
            </svg>
          </div>
          <div>
            <h2>
              {{ currentData[index].name }}
              <button
                class="btn btn-secondary"
                data-bs-toggle="modal"
                :data-bs-target="'#data' + result.id"
              >
                Update {{ type }}
              </button>
            </h2>
            <p>{{ currentData[index].description }}</p>
            <div>
              <div
                class="modal fade"
                :id="['data' + result.id]"
                tabindex="-1"
                aria-labelledby="label"
                aria-hidden="true"
              >
                <div class="modal-dialog modal-lg">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h5 class="modal-title" id="label">
                        Update Value/Principle
                      </h5>
                      <button
                        type="button"
                        class="btn-close"
                        data-bs-dismiss="modal"
                        aria-label="Close"
                      ></button>
                    </div>
                    <form
                      @submit.prevent="
                        this.submitForm(
                          result.id,
                          results[index].name,
                          results[index].description
                        )
                      "
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
                            v-model="results[index].name"
                            required
                          />
                          <div class="invalid-feedback">
                            Valid first name is required.
                          </div>
                        </div>
                        <div>
                          <label for="description" class="form-label"
                            >Description</label
                          >
                          <textarea
                            type="text"
                            class="form-control"
                            id="description"
                            placeholder=""
                            v-model="results[index].description"
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
          </div>
        </div>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: { type: String, list_reload: Number },
  data() {
    return {
      results: [],
      currentData: [],
      currentDescription: [],
    };
  },
  methods: {
    async loadData() {
      const response = await axios.get(
        `http://localhost:8000/api/v1/${this.type}/`
      );
      response.data.map((result) => {
        this.currentData.push({
          id: result.id,
          name: result.name,
          description: result.description,
        });
      });
      this.results = response.data;
    },
    async submitForm(id, name, description) {
      await axios.patch(`http://localhost:8000/api/v1/${this.type}/${id}/`, {
        name: name,
        description: description,
      });
      this.$emit("submitForm");
    },
  },
  mounted() {
    this.loadData();
  },
};
</script>
