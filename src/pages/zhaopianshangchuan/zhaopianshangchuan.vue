<script setup>
  import { useRouter } from 'vue-router';
  import { reactive, onMounted } from 'vue';

  const props = defineProps({});

  const data = reactive({
    v_model: '',
  });

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
          <span class="font" @click="onClick">主页</span>
          <div class="flex-row ml-63">
            <span class="font text_2" @click="onClick_1">登录注册</span>
            <span class="font text_3 ml-53" @click="onClick_2">类别创建</span>
            <span class="font ml-53">照片上传</span>
            <span class="font text_4 ml-53" @click="onClick_3">图像生成</span>
            <span class="font text_5 ml-53" @click="onClick_4">相册展示</span>
          </div>
        </div>
      </div>
      <span class="text_6">未登录</span>
    </div>
    <div class="flex-col section section_2">
      <img
        class="image"
        src="https://ide.code.fun/api/image?token=6662d7b6a16e9e001251f0b6&name=8e57acb8fdb995a693fc68463f25106a.png"
      />
      <div class="flex-col section_3 mt-20">
        <div class="flex-col self-center">
          <span class="self-start text_7">凝时绘影 照片上传</span>
          <span class="self-center text_8 mt-21">请上传您的照片并指定类别</span>
        </div>
        <div class="flex-col self-stretch group_2">
          <span class="self-start font text_9">照片标题</span>
          <el-input class="input mt-14 elinput" v-model="data.v_model"></el-input>
        </div>
        <div class="flex-col self-stretch group_3">
          <span class="self-start font text_11">类别</span>
          <div class="flex-row justify-between items-center section_5 mt-14">
            <div class="flex-col justify-start items-end group_1">
              <img
                class="self-start image_4"
                src="https://ide.code.fun/api/image?token=6662d7b6a16e9e001251f0b6&name=7820f75efe4be75e2b05434d901b355d.png"
              />
            </div>
            <div class="flex-row items-center group_4">
              <div class="section_6"></div>
              <span class="font text_12 ml-14">自动分类</span>
            </div>
          </div>
        </div>
        <div class="flex-col items-start self-stretch group_5">
          <span class="font text_13">凝时绘影 照片上传</span>
          <img
            class="image_5 mt-8"
            src="https://ide.code.fun/api/image?token=6662d7b6a16e9e001251f0b6&name=a8dca04ade96f8b8f9aa82aae0a32183.png"
          />
        </div>
        <div class="flex-col justify-start items-center self-stretch text-wrapper_2">
          <span class="text_14">上传</span>
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
  .mt-21 {
    margin-top: 1.31rem;
  }
  .page {
    padding-bottom: 1.25rem;
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
    background-color: #121212;
    overflow: hidden;
    width: 100%;
  }
  .image {
    width: 100vw;
    height: 22.2222vw;
  }
  .section_3 {
    padding: 2.45rem 22.47rem 2.5rem;
  }
  .text_7 {
    color: #ffffff;
    font-size: 3rem;
    font-family: HarmonyOSSansSC;
    font-weight: 700;
    line-height: 3.5rem;
    text-align: center;
    width: 30rem;
    height: 3.5rem;
  }
  .text_8 {
    color: #ffffff;
    font-size: 1.13rem;
    font-family: HarmonyOSSansSC;
    line-height: 1.06rem;
  }
  .group_2 {
    margin-top: 4.52rem;
  }
  .text_9 {
    line-height: 0.91rem;
  }
  .input {
    align-self: stretch;
  }
  .group_3 {
    margin-top: 2.76rem;
  }
  .text_11 {
    line-height: 0.91rem;
  }
  .section_5 {
    padding: 0.5rem 0.75rem;
    background-color: #383838;
    border-radius: 0.75rem;
  }
  .group_1 {
    padding: 0.41rem 0;
    width: 23.63rem;
  }
  .image_4 {
    width: 6.19rem;
    height: 1.19rem;
  }
  .group_4 {
    margin-right: 3.25rem;
    padding-left: 0.75rem;
    padding-right: 0.72rem;
  }
  .section_6 {
    background-color: #ffffff14;
    border-radius: 0.25rem;
    overflow: hidden;
    width: 1.13rem;
    height: 1.13rem;
  }
  .text_12 {
    line-height: 0.94rem;
  }
  .group_5 {
    margin-right: 1.06rem;
    margin-top: 5.75rem;
  }
  .text_13 {
    line-height: 1.5rem;
    width: 10rem;
  }
  .image_5 {
    border-radius: 0.75rem;
    height: 17.88rem;
  }
  .text-wrapper_2 {
    margin-top: 4.44rem;
    padding: 0.99rem 0 1.09rem;
    background-color: #800080;
    border-radius: 0.75rem;
  }
  .text_14 {
    color: #ffffff;
    font-size: 1.25rem;
    font-family: HarmonyOSSansSC;
    line-height: 1.17rem;
  }
  .elinput {
    width: 7.06rem !important;
  }
</style>