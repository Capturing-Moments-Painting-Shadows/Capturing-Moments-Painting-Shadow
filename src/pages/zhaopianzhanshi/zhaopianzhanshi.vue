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

  function onClick_6() {
    router.push({ name: 'zhaopiancaozuo' });
  }

  function onClick_7() {
    router.push({ name: 'zhaopiancaozuo' });
  }

  function onClick_8() {
    router.push({ name: 'zhaopiancaozuo' });
  }

  function onClick_9() {
    router.push({ name: 'zhaopiancaozuo' });
  }

  function onClick_10() {
    router.push({ name: 'zhaopiancaozuo' });
  }

  function onClick_11() {
    router.push({ name: 'zhaopiancaozuo' });
  }
</script>

<template>
  <div class="flex-col page">
    <div class="flex-row justify-between items-center header">
      <div class="flex-row items-center">
        <div class="flex-col justify-start text-wrapper"><span class="text">凝时绘影</span></div>
        <div class="flex-row group_1 ml-40-5">
          <span class="font" @click="onClick">主页</span>
          <div class="flex-row shrink-0 group_5 ml-31-5">
            <span class="font text_2" @click="onClick_1">登录注册</span>
            <span class="font text_3 ml-26" @click="onClick_2">类别创建</span>
            <span class="font ml-26" @click="onClick_3">照片上传</span>
            <span class="font text_4 ml-26" @click="onClick_4">图像生成</span>
            <span class="font text_5 ml-26" @click="onClick_5">相册展示</span>
          </div>
        </div>
      </div>
      <span class="text_6">未登录</span>
    </div>
    <div class="flex-col section section_2">
      <span class="self-center text_7">风景照</span>
      <div class="flex-row self-stretch group">
        <img
          class="image"
          src="https://ide.code.fun/api/image?token=6662d7b6a16e9e001251f0b6&name=205486bd998e43e336e6f6b0c5266bd6.png"
        />
        <img
          class="image ml-13-5"
          src="https://ide.code.fun/api/image?token=6662d7b6a16e9e001251f0b6&name=5020e0204f7a54681d0b5a73b036045f.png"
        />
        <img
          class="image ml-13-5"
          src="https://ide.code.fun/api/image?token=6662d7b6a16e9e001251f0b6&name=b64d74a4134b3de75e1a8b5340aa4e1e.png"
        />
      </div>
      <div class="flex-row justify-between self-stretch section_3 view">
        <span class="font_2" @click="onClick_6">照片1</span>
        <span class="font_2" @click="onClick_7">照片2</span>
        <span class="font_2" @click="onClick_8">照片3</span>
      </div>
      <div class="flex-row self-stretch group_2">
        <img
          class="image"
          src="https://ide.code.fun/api/image?token=6662d7b6a16e9e001251f0b6&name=ad80034784574a70778c94cd92579325.png"
        />
        <img
          class="image ml-13-5"
          src="https://ide.code.fun/api/image?token=6662d7b6a16e9e001251f0b6&name=aab6b567d1adcf40741b20ae0fd1d639.png"
        />
        <img
          class="image ml-13-5"
          src="https://ide.code.fun/api/image?token=6662d7b6a16e9e001251f0b6&name=b1925c4f57210a7d7c22a85d3594b113.png"
        />
      </div>
      <div class="flex-row justify-between self-stretch section_3">
        <span class="font_2" @click="onClick_9">照片4</span>
        <span class="font_2" @click="onClick_10">照片5</span>
        <span class="font_2" @click="onClick_11">照片6</span>
      </div>
    </div>
  </div>
</template>

<style scoped lang="css">
  .ml-40-5 {
    margin-left: 2.53rem;
  }
  .ml-31-5 {
    margin-left: 1.97rem;
  }
  .ml-13-5 {
    margin-left: 0.84rem;
  }
  .page {
    background-color: #000000;
    width: 100%;
    overflow-y: auto;
    overflow-x: hidden;
    height: 100%;
  }
  .header {
    padding: 0.5rem 2.5rem 0.5rem;
    background-color: #121212;
    overflow: hidden;
  }
  .text-wrapper {
    padding: 0.23rem 0 0.36rem;
    border-radius: 0.19rem;
    height: 1.25rem;
  }
  .text {
    color: #ffffff;
    font-size: 0.69rem;
    font-family: Kalam;
    font-weight: 700;
    line-height: 0.65rem;
  }
  .group_1 {
    width: 19.8rem;
  }
  .font {
    font-size: 0.5rem;
    font-family: HarmonyOSSansSC;
    line-height: 0.47rem;
    color: #ffffff;
  }
  .group_5 {
    width: 16.83rem;
  }
  .text_2 {
    line-height: 0.47rem;
  }
  .text_3 {
    line-height: 0.47rem;
  }
  .text_4 {
    line-height: 0.47rem;
  }
  .text_5 {
    line-height: 0.46rem;
  }
  .text_6 {
    margin-right: 0.7rem;
    color: #fcfcfc;
    font-size: 0.63rem;
    font-family: IdeaFonts MeiLingTi;
    line-height: 0.56rem;
  }
  .section {
    flex-grow: 1;
  }
  .section_2 {
    padding: 2.71rem 2.44rem 4.22rem;
    background-color: #121212;
    overflow: hidden;
    width: 100%;
  }
  .text_7 {
    color: #ffffff;
    font-size: 1.75rem;
    font-family: HarmonyOSSansSC;
    font-weight: 700;
    line-height: 1.59rem;
  }
  .group {
    margin-top: 2.13rem;
  }
  .image {
    flex: 1 1 12.78rem;
    border-radius: 0.25rem;
    height: 9.41rem;
  }
  .section_3 {
    padding: 0.9rem 5.04rem 0.96rem 5.12rem;
    background-color: #383838;
    overflow: hidden;
  }
  .view {
    margin-top: 1.86rem;
  }
  .font_2 {
    font-size: 0.75rem;
    font-family: IdeaFonts MeiLingTi;
    line-height: 0.66rem;
    color: #ffffff;
  }
  .group_2 {
    padding: 1.86rem 0 1.86rem;
  }
</style>