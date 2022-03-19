const {createApp} = Vue;
const CoinApp = {
    data() {
        return {coins: null, message: 'message'}
    },
    created() {
        const socket = new WebSocket(`ws://${window.location.host}/ws/coins/`)
        let _this = this
        socket.onmessage = function (event) {
            _this.coins = JSON.parse(event.data)
        }
    }
}

createApp(CoinApp).mount('#app')