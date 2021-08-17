import AddModal from "@/components/AddModal.vue"
import { mount } from "@vue/test-utils"
import axios from "axios"

jest.mock('axios', () => ({
    post: jest.fn(() => {})
}))


describe("addModal.vue", () => {
    let wrapper = mount(AddModal, {
        data() {
            return {
                type: "values",
                title: "initial value",
                description: "initial description"
            }
        }
    })

    it("shows modal total", () => {
        expect(wrapper.find("h5").text()).toBe("Add Value/Principle")
    })

    it("mocks axios post request and submit function", async() => {
        const title = "Test title"
        const description = "Test description"

        await wrapper.find("input").setValue(title)
        await wrapper.find("textarea").setValue(description)
        await wrapper.find('form').trigger('submit.prevent')

        expect(axios.post).toHaveBeenCalledTimes(1)

        const titleField = await wrapper.get("input")
        const descriptionField = await wrapper.get("textarea")

        expect(titleField.text()).toBe("")
        expect(descriptionField.text()).toBe("")

        expect(wrapper.emitted()).toHaveProperty("submitForm")


    })
    it('renders correctly', () => {
        const wrapper = mount(AddModal)
        expect(wrapper.element).toMatchSnapshot()
    })
})