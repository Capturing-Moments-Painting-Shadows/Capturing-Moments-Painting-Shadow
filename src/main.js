import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store'; // 导入 Vuex Store
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';

const app = createApp(App);
app.use(ElementPlus);
app.use(router);
app.use(store); // 使用 Vuex Store

app.mount('#app');
