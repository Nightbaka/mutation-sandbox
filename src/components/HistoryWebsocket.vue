<template>
    <!-- <div>
      <button @click="sendData">Send Data</button>
    </div> -->
  </template>
  
  <script>
  export default {
    name: 'HistoryWebsocket',
    data() {
      return {
        socket: null,
      };
    },
    methods: {
      connectWebSocket() {
        this.socket = new WebSocket('ws://localhost:8000/ws/experiment/');
  
        this.socket.onopen = () => {
          console.log('WebSocket connected');
        };
  
        this.socket.onmessage = (event) => {
          const message = JSON.parse(event.data);
          console.log('Message from server:', message);
          this.$emit('update-runs', data)
        };
  
        this.socket.onclose = () => {
          console.log('WebSocket disconnected');
        };
      },
      sendData() {
        if (this.socket) {
          this.socket.send(JSON.stringify({ message: 'Hello, server!' }));
        }
      }
    },
    mounted() {
      this.connectWebSocket();
    }
  };
  </script>
  