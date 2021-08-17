import HomePage from "@/components/HomePage.vue";
import { shallowMount } from "@vue/test-utils";


describe("homePage.vue", () => {

    let wrapper = shallowMount(HomePage);

    it("shows title header of the app", () => {
        expect(wrapper.find("h1").text()).toBe("Values and Principles of Agile Software Development")
    })

    it('renders correctly', () => {
        expect(wrapper.element).toMatchSnapshot()
    })
});