<script setup>
  import { useRouter } from 'vue-router';
  import { reactive, onMounted } from 'vue';
  import axios from 'axios';

  const props = defineProps({});

  const router = useRouter();

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

  const data = reactive({
    username: '',
    password: ''
  });

  const register = async () => {
    try {
      const response = await axios.post('http://localhost:5003/register', {
        username: data.username,
        password: data.password
      });
      console.log('Response:', response);
      if (response && response.data) {
        if (response.status === 201) {
          console.log(response.data.message);
          // handle the success, e.g., show success message to the user
          alert('注册成功！'); // 显示注册成功消息给用户
          // Redirect to login page
          router.push('/denglu'); // 跳转到登录页面
        } else {
          console.error('Unexpected response format:', response);
        }
      }
    } catch (error) {
      if (error.response && error.response.data) {
        console.error('Error response data:', error.response.data);
        // handle the error, e.g., show error message to the user
        alert(error.response.data.message); // 显示错误消息给用户
      } else {
        console.error('Unexpected error:', error);
      }
    }
  };
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
          <span class="text_13">欢迎注册</span>
          <span class="font_2 text_16 mt-38">欢迎加入凝时绘影</span>
        </div>
      </div>
      <div class="flex-col self-start section_5 ml-99">
        <div class="flex-col items-start">
          <span class="text_8">欢迎加入凝时绘影</span>
          <span class="font_2 text_9 mt-15">记录美好瞬间，留存珍贵回忆</span>
        </div>
        <div class="mt-42 flex-col">
          <span class="self-start font">用户名</span>
          <el-input class="mt-14 text-wrapper_2 elinput" placeholder="请输入用户名" v-model="data.username"></el-input>
        </div>
        <div class="mt-42 flex-col">
          <span class="self-start font text_10">密码</span>
          <div class="mt-14 flex-col self-stretch">
            <div class="flex-col self-stretch">
              <el-input v-model="data.password" class="elinput_1" placeholder="请输入密码"></el-input>
              <div @click="register" class="mt-12 flex-col justify-start items-center text-wrapper_3">
                <span class="text_12">注册</span>
              </div>
            </div>
            <span class="self-center font text_15 mt-8" @click="onClick_1">已有账号？登录账号</span>
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
    background-color: #121212;
    width: 100%;
    overflow-y: auto;
    overflow-x: hidden;
    height: 100%;
  }
  .header {
    padding: 1rem 5rem 0.91rem;
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
    font-size: 1rem;
    font-family: "Noto Serif SC", serif;;
    line-height: 0.94rem;
    color: #ffffff;
  }
  .text_2 {
    line-height: 0.94rem;
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
    font-family: "Noto Serif SC", serif;;
    line-height: 1.11rem;
  }
  .section {
    flex-grow: 1;
  }
  .section_2 {
    padding-top: 0.094rem;
    background-color: #121212;
    overflow: hidden;
    width: 100%;
  }
  .section_3 {
    background-image: url('https://picture.gptkong.com/20240610/00144ff89bd7bc443599ad34e0916e9918.png');
    background-size: 100% 100%;
    background-repeat: no-repeat;
    width: 45rem;
    height: 49.25rem;
  }
  .section_4 {
    padding: 30.68rem 0 11.8rem;
    background-image: linear-gradient(0deg, #00000000 100%, #090630e6 -15.2%);
    width: 45rem;
  }
  .text_13 {
    color: #ffffff;
    font-size: 3.5rem;
    font-family: "Noto Serif SC", serif;;
    font-weight: 700;
    line-height: 3.34rem;
  }
  .font_2 {
    font-size: 1.13rem;
    font-family: "Noto Serif SC", serif;;
    color: #ffffff;
  }
  .text_16 {
    line-height: 1.04rem;
  }
  .section_5 {
    margin-top: 7.63rem;
    padding: 3.24rem 2.75rem 6.71rem 3rem;
    background-color: #ffffff14;
    border-radius: 1.25rem;
    height: 35.25rem;
    border: solid 0.063rem #ffffff29;
  }
  .text_8 {
    color: #ffffff;
    font-size: 2.5rem;
    font-family: "Noto Serif SC", serif;;
    font-weight: 700;
    line-height: 2.35rem;
  }
  .text_9 {
    line-height: 1.14rem;
  }
  .input_1 {
    align-self: stretch;
    margin-right: 0.13rem;
  }
  .font_3 {
    font-size: 1rem;
    font-family: "Noto Serif SC", serif;;
    line-height: 0.94rem;
    color: #ffffff99;
  }
  .text_11 {
    line-height: 0.92rem;
  }
  .input {
    margin-right: 0.13rem;
    padding: 1.12rem 0 1.21rem;
    background-color: #ffffff1a;
    border-radius: 0.75rem;
    width: 26.5rem;
  }
  .text_12 {
    margin-left: 0.8rem;
    line-height: 0.92rem;
    color: #ffffff;
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
  .text_14 {
    color: #ffffff;
    font-size: 1.25rem;
    font-family: "Noto Serif SC", serif;;
    line-height: 1.17rem;
  }
  .text_15 {
    line-height: 0.92rem;
  }
  .elinput {
    width: 26.5rem !important;
  }
</style>