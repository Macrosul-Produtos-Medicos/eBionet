const Suporte = () => ({
    AC: true,
    AM: false,
    show_guide_list: [],
    guides : [],
    init(){
        this.getGuideList()
        this.__setShowGuideList()
    },

    async getGuideList(){
        const url = `/suporte/api/get-guide-list/`
        const response = await axios.get(url)
        this.guides = response.data.guides
    },

    __setShowGuideList(){
        this.guides.forEach((guide, index) => {
            this.show_guide_list.push(false)
        })
    }
})