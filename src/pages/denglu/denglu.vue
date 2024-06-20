<script setup>
  import { useRouter } from 'vue-router';
  import { reactive } from 'vue';
  import { useStore } from 'vuex';
  import axios from 'axios';

  const props = defineProps({});

  const data = reactive({
    username: '',
    password: '',
  });

  const store = useStore();
  const router = useRouter();

  const login = async () => {
    try {
      const response = await axios.post('http://localhost:5000/login', {
        username: data.username,
        password: data.password
      });
      console.log('Response:', response);
      if (response && response.data) {
        if (response.status === 200) {
          console.log(response.data.message);
          // 保存 userId 和 username 到 Vuex Store
          store.dispatch('login', { ...response.data.user, id: response.data.userId, username: data.username });
          // 显示登录成功消息给用户
          alert('登录成功！');
          // 跳转到主页面
          router.push('/');
        } else {
          console.error('Unexpected response format:', response);
        }
      }
    } catch (error) {
      if (error.response && error.response.data) {
        console.error('Error response data:', error.response.data);
        // 显示错误消息给用户
        alert(error.response.data.message);
      } else {
        console.error('Unexpected error:', error);
      }
    }
  };

  function onClick() {
    router.push({ name: 'zhuye' });
  }

  function onClick_1() {
    router.push({ name: 'denglu' });
  }

  function onClick_2() {
    router.push({ name: 'leibiechuangjian' });
  }

  function onClick_3() {
    router.push({ name: 'zhaopianshangchuan' });
  }

  function onClick_4() {
    router.push({ name: 'Page_group_tuxiangshengcheng' });
  }

  function onClick_5() {
    router.push({ name: 'xiangcezhanshi' });
  }

  function onClick_6() {
    router.push({ name: 'zhuce' });
  }
</script>

<template>
  <div class="flex-col page">
    <div class="flex-row justify-between items-center header">
      <div class="flex-row items-center">
        <div class="flex-col justify-start text-wrapper"><span class="text">凝时绘影</span></div>
        <div class="flex-row ml-81">
          <span class="font text_3 ml-53" @click="onClick">主页</span>
          <div class="flex-row ml-63">
            <span class="font text_3 ml-53" @click="onClick_1">登录注册</span>
            <span class="font text_3 ml-53" @click="onClick_2">类别创建</span>
            <span class="font text_3 ml-53" @click="onClick_3">照片上传</span>
            <span class="font text_3 ml-53" @click="onClick_4">图像生成</span>
            <span class="font text_3 ml-53" @click="onClick_5">相册展示</span>
          </div>
        </div>
      </div>

    </div>
    <div class="flex-row justify-center section section_2">
      <div class="flex-col justify-start section_3">
        <div class="flex-col items-center section_4">
          <span class="text_8">欢迎加入凝时绘影</span>
          <span class="font_2 mt-38">记录美好瞬间，留存珍贵回忆</span>
        </div>
      </div>
      <div class="flex-col self-center section_5 ml-99">
        <div class="flex-col items-start">
          <span class="text_8">欢迎加入凝时绘影</span>
          <span class="font_2 mt-15">记录美好瞬间，留存珍贵回忆</span>
        </div>
        <div class="mt-42 flex-col">
          <span class="self-start font">用户名</span>
          <el-input class="mt-14 text-wrapper_2 elinput" v-model="data.username" placeholder="请输入用户名"></el-input>
        </div>
        <div class="mt-42 flex-col">
          <span class="self-start font text_10">密码</span>
          <div class="mt-14 flex-col self-stretch">
            <div class="flex-col self-stretch">
              <el-input v-model="data.password" class="elinput_1" placeholder="请输入密码"></el-input>
              <div @click="login" class="mt-12 flex-col justify-start items-center text-wrapper_3">
                <span class="text_12">登录</span>
              </div>
            </div>
            <span class="self-center font_1 mt-8" @click="onClick_6">没有账号？注册账号</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="css">
  .ml-81 {
    margin-left: 5.06rem;
  }
  .ml-63 {
    margin-left: 3.94rem;
  }
  .ml-53 {
    margin-left: 3.31rem;
  }
  .ml-99 {
    margin-left: 6.19rem;
  }
  .mt-15 {
    margin-top: 0.94rem;
  }
  .page {
    background-color: #000000;
    width: 100%;
    overflow-y: auto;
    overflow-x: hidden;
    height: 100%;
  }
  .header {
    padding: 1rem 5rem 1rem;
    background-color: #121212;
    overflow: hidden;
  }
  .text-wrapper {
    padding: 0.47rem 0 0.72rem;
    border-radius: 0.38rem;
    height: 2.5rem;
  }
  .text {
    margin-left: 0.22rem;
    margin-right: 0.21rem;
    color: #ffffff;
    font-size: 1.38rem;
    font-family: "Noto Serif SC", serif;
    font-weight: 700;
    line-height: 1.31rem;
  }
  .font {
    color: #ffffff;
    font-size: 1rem;
    line-height: 0.94rem;
    font-family: "Noto Serif SC", serif;
  }
  .font_1 {
    font-size: 1rem;
    font-family: "Noto Serif SC", serif;
    line-height: 0.94rem;
    color: #ffffff;
  }
  .text_3 {
    line-height: 0.94rem;
  }
  .text_4 {
    line-height: 0.94rem;
  }
  .text_5 {
    line-height: 0.93rem;
  }
  .text_6 {
    line-height: 0.92rem;
  }
  .text_7 {
    margin-right: 1.39rem;
    color: #fcfcfc;
    font-size: 1.25rem;
    font-family: "Noto Serif SC", serif;
    line-height: 1.11rem;
  }
  .section {
    flex-grow: 1;
  }
  .section_2 {
    background-color: #1d2129;
    overflow: hidden;
    width: 100%;
  }
  .section_3 {
    margin-bottom: -5rem;
    padding-bottom: 5rem;
    background-image: url('https://picture.gptkong.com/20240610/00138a0565ede2419f85b2148a2030c53a.png');
    background-size: 100% 100%;
    background-repeat: no-repeat;
    width: 45rem;
    height: 51.88rem;
  }
  .section_4 {
    padding: 29.05rem 0 11.06rem;
    background-image: linear-gradient(0deg, #00000000 100%, #090630e6 -15.2%);
    width: 45rem;
  }
  .text_12 {
    margin-left: 0.8rem;
    line-height: 0.92rem;
    color: #ffffff;
  }
  .font_2 {
    font-size: 1.13rem;
    font-family: "Noto Serif SC", serif;
    line-height: 1.14rem;
    color: #ffffff;
  }
  .section_5 {
    padding: 3.24rem 2.75rem 6.7rem 3rem;
    background-color: #ffffff14;
    border-radius: 1.25rem;
    height: 35.25rem;
    border: solid 0.063rem #ffffff29;
  }
  .text_8 {
    color: #ffffff;
    font-size: 2.5rem;
    font-family: "Noto Serif SC", serif;
    font-weight: 700;
    line-height: 2.35rem;
  }
  .input_1 {
    align-self: stretch;
    margin-right: 0.13rem;
  }
  .text_10 {
    line-height: 0.92rem;
  }
  .input_2 {
    margin-right: 0.13rem;
  }
  .text-wrapper_3 {
    margin-right: 0.13rem;
    padding: 0.98rem 0 1.09rem;
    background-color: #800080;
    border-radius: 0.75rem;
    width: 26.5rem;
    cursor: pointer; /* 确保它像按钮一样可点击 */
    text-align: center; /* 确保文字居中 */
  }
  .text_13 {
    color: #ffffff;
    font-size: 1.25rem;
    font-family: "Noto Serif SC", serif;
    line-height: 1.12rem;
  }
  .elinput {
    width: 26.5rem !important;
  }
  .elinput_1 {
    width: 26.5rem !important;
  }
</style>
