<script setup>
  import { useRouter } from 'vue-router';
  import { reactive, onMounted } from 'vue';

  const props = defineProps({});

  const data = reactive({
    v_model: '',
    v_model_1: '',
  });

  const router = useRouter();

  function onClick() {
    router.push({ name: 'zhuye' });
  }

  function onClick_1() {
    router.push({ name: 'denglu' });
  }

  function onClick_2() {
    router.push({ name: 'zhaopianshangchuan' });
  }

  function onClick_3() {
    router.push({ name: 'Page_group_tuxiangshengcheng' });
  }

  function onClick_4() {
    router.push({ name: 'xiangcezhanshi' });
  }
</script>

<template>
  <div class="flex-col page">
    <div class="flex-row justify-between items-center header">
      <div class="flex-row items-center">
        <div class="flex-col justify-start text-wrapper"><span class="text">凝时绘影</span></div>
        <div class="flex-row ml-81">
          <span class="font text_2" @click="onClick">主页</span>
          <div class="flex-row ml-63">
            <span class="font text_3" @click="onClick_1">登录注册</span>
            <span class="font text_4 ml-53">类别创建</span>
            <span class="font text_5 ml-53" @click="onClick_2">照片上传</span>
            <span class="font text_6 ml-53" @click="onClick_3">图像生成</span>
            <span class="font text_7 ml-53" @click="onClick_4">相册展示</span>
          </div>
        </div>
      </div>
      <span class="text_8">未登录</span>
    </div>
    <div class="flex-col items-center section section_2">
      <img
        class="image"
        src="https://ide.code.fun/api/image?token=6662d7b6a16e9e001251f0b6&name=a8ff8364a4078f1cc470493bc322fdb4.png"
      />
      <div class="flex-col mt-83">
        <div class="flex-col items-center">
          <span class="text_9">创建新类别</span>
          <span class="text_10 mt-28">请输入新类别的名称和描述</span>
        </div>
        <div class="flex-col mt-90">
          <span class="self-start font">类别名称</span>
          <el-input class="input_1 elinput" v-model="data.v_model"></el-input>
          <span class="self-start font text_12">类别描述</span>
          <div class="flex-col self-stretch group">
            <el-input v-model="data.v_model_1" class="elinput_1"></el-input>
            <div class="flex-col justify-start items-center text-wrapper_3 mt-16">
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
    font-family: Kalam;
    font-weight: 700;
    line-height: 1.31rem;
  }
  .font {
    font-size: 1rem;
    font-family: HarmonyOSSansSC;
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
    font-family: IdeaFonts MeiLingTi;
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
    font-family: HarmonyOSSansSC;
    font-weight: 700;
    line-height: 2.87rem;
  }
  .text_10 {
    color: #ffffff;
    font-size: 1.13rem;
    font-family: HarmonyOSSansSC;
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
  }
  .text_14 {
    color: #ffffff;
    font-size: 1.25rem;
    font-family: HarmonyOSSansSC;
    line-height: 1.17rem;
  }
  .elinput {
    width: 45rem !important;
  }
  .elinput_1 {
    width: 45rem !important;
  }
</style>