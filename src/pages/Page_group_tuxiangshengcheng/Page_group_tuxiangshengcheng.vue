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
    router.push({ name: 'zhaopianshangchuan' });
  }

  function onClick_4() {
    router.push({ name: 'xiangcezhanshi' });
  }

  function onClick_5() {
    router.push({ name: 'zhaopiancaozuo' });
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
            <span class="font text_4 ml-53" @click="onClick_2">类别创建</span>
            <span class="font text_5 ml-53" @click="onClick_3">照片上传</span>
            <span class="font ml-53">图像生成</span>
            <span class="font text_6 ml-53" @click="onClick_4">相册展示</span>
          </div>
        </div>
      </div>
      <span class="text_7">未登录</span>
    </div>
    <div class="flex-col section section_2">
      <img
        class="image"
        src="https://ide.code.fun/api/image?token=6662d7b6a16e9e001251f0b6&name=2d1bd6e380591000249c4a91c42ee364.png"
      />
      <div class="flex-row justify-center section_3">
        <div class="flex-col justify-start items-center self-start text-wrapper_2">
          <span class="text_12">拖入照片或点击选择</span>
        </div>
        <div class="flex-col section_4 ml-14">
          <div class="flex-col items-center">
            <span class="text_8">图像生成</span>
            <span class="text_9 mt-29">请输入图像相关信息</span>
          </div>
          <div class="flex-col group">
            <span class="self-start font text_10">图像名称</span>
            <el-input class="input mt-14 elinput" v-model="data.v_model"></el-input>
          </div>
          <div class="flex-col group_2">
            <span class="self-start font text_1">图像生成</span>
            <div class="flex-col self-stretch mt-14">
              <div class="flex-col justify-start items-start text-wrapper_4">
                <span class="font_2 text_13">请输入生成图像的描述词</span>
              </div>
              <div class="flex-col justify-start items-center text-wrapper_5 mt-16" @click="onClick_5">
                <span class="text_14">生成图像</span>
              </div>
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
  .mt-29 {
    margin-top: 1.81rem;
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
    line-height: 0.92rem;
  }
  .text_7 {
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
    padding: 1.94rem 4.31rem 1.31rem;
  }
  .text-wrapper_2 {
    margin-top: 7.84rem;
    padding: 16.64rem 0 14.72rem;
    border-radius: 0.5rem;
    background-image: url('https://ide.code.fun/api/image?token=6662d7b6a16e9e001251f0b6&name=20765bce71abde4e243181559ad97632.png');
    background-size: 100% 100%;
    background-repeat: no-repeat;
    width: 36.13rem;
    height: 33.38rem;
  }
  .text_12 {
    color: #ffffff;
    font-size: 2.25rem;
    font-family: IdeaFonts MeiLingTi;
    font-weight: 900;
    line-height: 2.02rem;
  }
  .section_4 {
    padding: 5.19rem 5.56rem 6.5rem;
    background-color: #121212;
    overflow: hidden;
    width: 44.38rem;
    height: 46.31rem;
  }
  .text_8 {
    color: #ffffff;
    font-size: 3rem;
    font-family: HarmonyOSSansSC;
    font-weight: 700;
    line-height: 2.84rem;
  }
  .text_9 {
    color: #ffffff;
    font-size: 1.13rem;
    font-family: HarmonyOSSansSC;
    line-height: 1.05rem;
  }
  .group {
    margin-top: 4.21rem;
  }
  .text_10 {
    margin-left: 0.098rem;
    line-height: 0.93rem;
  }
  .input {
    align-self: stretch;
  }
  .font_2 {
    font-size: 1rem;
    font-family: HarmonyOSSansSC;
    line-height: 0.93rem;
    color: #505050;
  }
  .group_2 {
    margin-top: 2.74rem;
  }
  .text_1 {
    margin-left: 0.098rem;
  }
  .text-wrapper_4 {
    padding: 0.99rem 0 9.33rem;
    background-color: #ffffff1a;
    border-radius: 0.75rem;
    width: 33.25rem;
  }
  .text_13 {
    margin-left: 0.8rem;
  }
  .text-wrapper_5 {
    padding: 0.99rem 0 1.1rem;
    background-color: #800080;
    border-radius: 0.75rem;
    width: 33.25rem;
  }
  .text_14 {
    color: #ffffff;
    font-size: 1.25rem;
    font-family: HarmonyOSSansSC;
    line-height: 1.16rem;
  }
  .elinput {
    width: 33.25rem !important;
  }
</style>