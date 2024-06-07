<script setup>
  import { useRouter } from 'vue-router';
  import { reactive, onMounted } from 'vue';

  const props = defineProps({});

  const data = reactive({});

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
</script>

<template>
  <div class="flex-col page">
    <div class="flex-row justify-between items-center header">
      <div class="flex-row items-center">
        <div class="flex-col justify-start text-wrapper"><span class="text">凝时绘影</span></div>
        <div class="flex-row ml-81">
          <span class="font" @click="onClick">主页</span>
          <div class="flex-row shrink-0 ml-63">
            <span class="font text_2" @click="onClick_1">登录注册</span>
            <span class="font text_3 ml-53" @click="onClick_2">类别创建</span>
            <span class="font ml-53" @click="onClick_3">照片上传</span>
            <span class="font text_4 ml-53" @click="onClick_4">图像生成</span>
            <span class="font text_5 ml-53" @click="onClick_5">相册展示</span>
          </div>
        </div>
      </div>
      <span class="text_6">未登录</span>
    </div>
    <div class="flex-col section section_2">
      <img
        class="shrink-0 image"
        src="https://ide.code.fun/api/image?token=6662d7b6a16e9e001251f0b6&name=45badbf1f468990ccbc2f71caefc843a.png"
      />
      <div class="flex-row justify-between group mt-64">
        <span class="self-start text_7">图片名</span>
        <div class="flex-col group_2">
          <span class="self-start text_8">请在此处添加照片的注释...</span>
          <el-button class="button mt-6 elbutton"></el-button>
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
    font-family: Kalam;
    font-weight: 700;
    line-height: 1.31rem;
  }
  .font {
    font-size: 1rem;
    font-family: HarmonyOSSansSC;
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
    font-family: IdeaFonts MeiLingTi;
    line-height: 1.11rem;
  }
  .section {
    flex-grow: 1;
  }
  .section_2 {
    padding: 5rem 5rem 5rem;
    background-color: #121212;
    overflow: hidden;
    width: 100%;
  }
  .image {
    border-radius: 1rem;
    width: 80rem;
    height: 43.75rem;
  }
  .group {
    padding-left: 0.24rem;
  }
  .text_7 {
    color: #ffffff;
    font-size: 3rem;
    font-family: HarmonyOSSansSC;
    font-weight: 700;
    line-height: 2.81rem;
  }
  .group_2 {
    width: 37.45rem;
  }
  .text_8 {
    color: #ffffff;
    font-size: 1.13rem;
    font-family: HarmonyOSSansSC;
    line-height: 1.05rem;
  }
  .button {
    align-self: flex-end;
  }
  .elbutton {
    width: 7.5rem !important;
  }
</style>