import List from "@/components/List.vue";
import flushPromises from "flush-promises";
import { shallowMount, mount } from "@vue/test-utils";

const axios = require('axios');

jest.mock("axios", () => ({
    get: () =>
        Promise.resolve({
            data: [
                { id: 1, title: "Mocked title", description: "Mocked description" },
            ],
        })
}));


describe("list.vue", () => {

    let wrapper = shallowMount(List);
    it("shows the update button", () => {
        expect(wrapper.find("button").text()).toBe("Update")
    })

    it("mocking the axios call to get list of entries", async() => {
        await flushPromises();
        expect(wrapper.vm.results.length).toBe(1);
    });

    it("does title div exists", async() => {
        await flushPromises();
        expect(wrapper.find("span").text()).toBe(wrapper.vm.results[0].title)
    })

    it("does paragraph description exists", async() => {
        await flushPromises();
        expect(wrapper.find("p").text()).toBe(wrapper.vm.results[0].description)
    })

    it('renders correctly', () => {
        const wrapper = mount(List)
        expect(wrapper.element).toMatchSnapshot()
    })

});