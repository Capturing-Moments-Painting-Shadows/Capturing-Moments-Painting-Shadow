<script setup>
  import { useRoute, useRouter } from 'vue-router';
  import { ref, reactive, onMounted } from 'vue';
  import axios from 'axios';
  import { ElButton, ElInput } from 'element-plus';

  const props = defineProps({});

  const data = reactive({
    description: ''
  });
  const photo_name = '银渐层';
  const router = useRouter();

  const routes = [
    'zhuye', 
    'denglu', 
    'leibiechuangjian', 
    'zhaopianshangchuan',
    'Page_group_tuxiangshengcheng', 
    'xiangcezhanshi'
  ];

  function navigateToRoute(index) {
    router.push({ name: routes[index] });
  }

  function deletePhoto() {
    // 实现删除照片的逻辑
    console.log('删除照片');
  }

  function submitDescription() {
    // 实现提交注释的逻辑
    console.log('提交注释', data.description);
  }
</script>

<template>
  <div class="flex-col page">
    <div class="flex-row justify-between items-center header">
      <div class="flex-row items-center">
        <div class="flex-col justify-start text-wrapper"><span class="text">凝时绘影</span></div>
        <div class="flex-row ml-81">
          <span class="font" @click="navigateToRoute(0)">主页</span>
          <div class="flex-row shrink-0 ml-63">
            <span class="font text_2" @click="navigateToRoute(1)">登录注册</span>
            <span class="font text_3 ml-26" @click="navigateToRoute(2)">类别创建</span>
            <span class="font ml-26" @click="navigateToRoute(3)">照片上传</span>
            <span class="font text_4 ml-26" @click="navigateToRoute(4)">图像生成</span>
            <span class="font text_5 ml-26" @click="navigateToRoute(5)">相册展示</span>
          </div>
        </div>
      </div>
      <span class="text_6">未登录</span>
    </div>
    <div class="flex-col section section_2">
      <div class="flex-row">
        <img
          class="shrink-0 image"
          src="https://ide.code.fun/api/image?token=6662d7b6a16e9e001251f0b6&name=45badbf1f468990ccbc2f71caefc843a.png"
        />
        <div class="description-box">
          <p class="description-text">{{ data.description }}</p>
        </div>
      </div>
      <div class="flex-row justify-between group mt-64">
        <div class="flex-row items-center">
          <span class="self-start text_7">{{ photo_name }}</span>
        </div>
        <div class="flex-row group_2">
          <el-input v-model="data.description" class="elinput_1" placeholder="请在此处添加照片的注释..."></el-input>
          <el-button class="button elbutton" @click="submitDescription">提交注释</el-button>
          <el-button class="delete-button" @click="deletePhoto">删除图片</el-button>
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
    font-size: 1rem;
    font-family: "Noto Serif SC", serif;
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
    line-height: 0.93rem;
  }
  .text_5 {
    line-height: 0.92rem;
  }
  .text_6 {
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
    padding: 2rem 5rem 5rem;
    background-color: #121212;
    overflow: hidden;
    width: 100%;
  }
  .image {
    border-radius: 1rem;
    width: 50rem;
    height: 33rem;
    margin-right: 2rem; /* 图片和描述框之间的间距 */
  }
  .description-box {
    flex-grow: 1;
    color: #ffffff;
    font-size: 1.25rem;
    font-family: "Noto Serif SC", serif;
    line-height: 1.5rem;
    background-color: #333333;

    border-radius: 0.5rem;
  }
  .description-text {
    white-space: pre-wrap; /* 保留换行符 */
  }
  .group {
    padding-left: 0.24rem;
  }
  .text_7 {
    color: #ffffff;
    font-size: 3rem;
    font-family: "Noto Serif SC", serif;
    font-weight: 700;
    line-height: 2.81rem;

  }
  .delete-button {
    color: #ff4d4f;
    border-color: #ff4d4f;
  }
  .group_2 {
    display: flex;
    justify-content: space-between;
    align-items: center; /* 垂直居中对齐 */
    gap: 1rem;
  }
  .text_8 {
    color: #ffffff;
    font-size: 1.13rem;
    font-family: "Noto Serif SC", serif;

  }
  .elbutton {
    width: 7.5rem !important;
  }
  .elinput_1 {
    width: 40rem;
  }
</style>
