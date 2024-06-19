<script setup>
  import { useRouter } from 'vue-router';
  import { reactive, computed } from 'vue'; // 确保导入 computed
  import { useStore } from 'vuex';
  import axios from 'axios';

  const props = defineProps({});

  const data = reactive({
    name: '',
    description: '',
  });

  const store = useStore();
  const router = useRouter();

  // 确保 store 已经初始化并且 state 存在
  const isAuthenticated = computed(() => store?.state?.isAuthenticated || false);
  const username = computed(() => store?.state?.username || '未登录');
  console.log("username:",username.value)
  console.log("isAuthenticated:",isAuthenticated.value)


  const create_category = async () => {
    if (!isAuthenticated.value) {
      alert('请先登录');
      router.push('/denglu');
      return;
    }

    try {
      const response = await axios.post('http://localhost:5000/create_category', {
        name: data.name,
        description: data.description,
        username: username.value,
      });
      console.log('Response:', response);
      if (response && response.data) {
        if (response.status === 201) {
          console.log(response.data.message);
          // 显示类别创建成功消息给用户
          alert('类别创建成功！');
          // 跳转到类别展示页面
          router.push('/zhaopianshangchuan');
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
      <div>
        <span class="font text_3 ml-53">
          {{ isAuthenticated ? username : '未登录' }}
        </span>
      </div>
    </div>
    <div class="flex-col items-center section section_2">
      <img
        class="image"
        src="https://picture.gptkong.com/20240610/00143238563c874ddb90724bcef281d6d8.png"
      />
      <div class="flex-col mt-83">
        <div class="flex-col items-center">
          <span class="text_9">创建新类别</span>
          <span class="text_10 mt-28">请输入新类别的名称和描述</span>
        </div>
        <div class="flex-col mt-90">
          <span class="self-start font">类别名称</span>
          <el-input class="input_1 elinput" v-model="data.name" placeholder="请输入类别名称"></el-input>
          <span class="self-start font text_12">类别描述</span>
          <div class="flex-col self-stretch group">
            <el-input v-model="data.description" class="elinput_1" placeholder="请输入类别描述"></el-input>
            <div @click="create_category" class="flex-col justify-start items-center text-wrapper_3 mt-16">
              <span class="text_14">创建类别</span>
            </div>
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
  .mt-83 {
    margin-top: 5.19rem;
  }
  .mt-90 {
    margin-top: 3rem;
  }
  .page {
    background-color: #000000;
    width: 100%;
    overflow-y: auto;
    overflow-x: hidden;
    height: 100%;
  }
  .header {
    padding: 1rem 5rem;
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
    font-family: "Noto Serif SC", serif;
    line-height: 0.93rem;
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
    line-height: 0.94rem;
  }
  .text_6 {
    line-height: 0.93rem;
  }
  .text_7 {
    line-height: 0.92rem;
  }
  .text_8 {
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
    padding-bottom: 7.75rem;
    background-color: #121212;
    overflow: hidden;
    width: 100%;
  }
  .image {
    width: 100vw;
    height: 16vw;
  }
  .text_9 {
    color: #ffffff;
    font-size: 3rem;
    font-family: "Noto Serif SC", serif;
    font-weight: 700;
    line-height: 2.87rem;
  }
  .text_10 {
    color: #ffffff;
    font-size: 1.13rem;
    font-family: "Noto Serif SC", serif;
    line-height: 1.05rem;
  }
  .input_1 {
    align-self: stretch;
    margin-top: 0.83rem;
  }
  .text_12 {
    margin-top: 1.75rem;
    line-height: 0.92rem;
  }
  .group {
    margin-top: 0.83rem;
  }
  .text-wrapper_3 {
    padding: 0.98rem 0 1.1rem;
    background-color: #800080;
    border-radius: 0.75rem;
    width: 45rem;
    cursor: pointer; /* 确保它像按钮一样可点击 */
    text-align: center; /* 确保文字居中 */
  }
  .text_14 {
    color: #ffffff;
    font-size: 1.25rem;
    font-family: "Noto Serif SC", serif;
    line-height: 1.17rem;
  }
  .elinput {
    width: 45rem !important;
  }
  .elinput_1 {
    width: 45rem !important;
  }
</style>
