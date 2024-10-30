const Suporte = () => ({
    AC: true,
    AM: false,
    show_states_list: [],
    show_guide_list: [],
    guides : [],
    assistances : [],
    init(){
        this.getGuideList()
        this.getAssistances()
        this.__setShowGuideList()
        this.__setShowStatesList()
    },

    async getGuideList(){
        const url = `/suporte/api/get-guide-list/`
        const response = await axios.get(url)
        this.guides = response.data.guides
    },

    async getAssistances(){
        const url = `/suporte/api/get-assistances/`
        const response = await axios.get(url)
        this.assistances = response.data.assistances
    },

    __setShowStatesList(){
        this.show_states_list[0] = true
        for (let i = 1; i < this.assistances.length; i++) {
            this.show_states_list[i] = false
        }
    },

    __setShowGuideList(){
        this.guides.forEach((guide, index) => {
            this.show_guide_list.push(false)
        })
    },

    closesTabs(idx){
        this.show_states_list.forEach((states, index) => {
            if (index != idx)
                this.show_states_list[index] = false
        })
    }
})