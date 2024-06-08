<script setup>
import { useRouter } from 'vue-router';
import { reactive } from 'vue';
import axios from 'axios';

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
  router.push({ name: 'zhaopianzhanshi' });
}

function onClick_6() {
  router.push({ name: 'zhaopianzhanshi' });
}

function onClick_7() {
  router.push({ name: 'zhaopianzhanshi' });
}

function onClick_8() {
  router.push({ name: 'zhaopianzhanshi' });
}

function onClick_9() {
  router.push({ name: 'zhaopianzhanshi' });
}

function onClick_10() {
  router.push({ name: 'zhaopianzhanshi' });
}
</script>

<template>
  <div class="flex-col page">
    <div class="flex-row justify-between items-center header">
      <div class="flex-row items-center">
        <div class="flex-col justify-start text-wrapper"><span class="text">凝时绘影</span></div>
        <div class="flex-row group_1 ml-40-5">
          <span class="font" @click="onClick">主页</span>
          <div class="flex-row shrink-0 group_6 ml-31-5">
            <span class="font text_2" @click="onClick_1">登录注册</span>
            <span class="font text_3 ml-26" @click="onClick_2">类别创建</span>
            <span class="font ml-26" @click="onClick_3">照片上传</span>
            <span class="font text_4 ml-26" @click="onClick_4">图像生成</span>
            <span class="font text_5 ml-26">相册展示</span>
          </div>
        </div>
      </div>
      <span class="text_6">未登录</span>
    </div>
    <div class="flex-col group section">
      <div class="flex-col section_2">
        <span class="self-center text_7">相册展示</span>
        <span class="self-center text_8">这里展示了我们最新的相册作品</span>
        <div class="flex-row self-stretch group_2">
          <img
            class="image"
            src="https://ide.code.fun/api/image?token=6662d7b6a16e9e001251f0b6&name=9859a8235a614cd9fca4ded2cb33ae1e.png"
          />
          <img
            class="image"
            src="https://ide.code.fun/api/image?token=6662d7b6a16e9e001251f0b6&name=9f5c087ce21f2c8cb52379d16e5ba492.png"
          />
          <img
            class="image"
            src="https://ide.code.fun/api/image?token=6662d7b6a16e9e001251f0b6&name=f69deb37630219993941c51ce007a5f6.png"
          />
        </div>
        <div class="flex-row justify-between align-center self-stretch section_3 view">
          <span class="font_2" @click="onClick_5">相册1</span>
          <span class="font_2" @click="onClick_6">相册2</span>
          <span class="font_2" @click="onClick_7">相册3</span>
        </div>
        <div class="flex-row self-stretch group_3">
          <img
            class="image"
            src="https://ide.code.fun/api/image?token=6662d7b6a16e9e001251f0b6&name=9859a8235a614cd9fca4ded2cb33ae1e.png"
          />
          <img
            class="image"
            src="https://ide.code.fun/api/image?token=6662d7b6a16e9e001251f0b6&name=9f5c087ce21f2c8cb52379d16e5ba492.png"
          />
          <img
            class="image"
            src="https://ide.code.fun/api/image?token=6662d7b6a16e9e001251f0b6&name=f69deb37630219993941c51ce007a5f6.png"
          />
        </div>
      </div>
      <div class="flex-col section">
        <div class="flex-col justify-start tabs-header">
          <div class="flex-row justify-between section_3 view_2">
            <span class="font_2" @click="onClick_8">相册4</span>
            <span class="font_2" @click="onClick_9">相册5</span>
            <span class="font_2" @click="onClick_10">相册6</span>
          </div>
        </div>
        <div class="group section_4"></div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="css">
  .ml-40-5 {
    margin-left: 5.06rem;
  }
  .ml-31-5 {
    margin-left: 3.94rem;
  }
  .ml-13-5 {
    margin-left: 16.8rem;
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
  .group_1 {
    width: 19.8rem;
  }
  .font {
    font-size: 1rem;
    font-family: "Noto Serif SC", serif;
    line-height: 0.94rem;
    color: #ffffff;
  }
  .group_6 {
    width: 16.83rem;
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
    margin-right: 1.39rem;
    color: #fcfcfc;
    font-size: 1.25rem;
    font-family: "Noto Serif SC", serif;
    line-height: 1.11rem;
  }
  .group {
    flex-grow: 1;
  }
  .section {
    width: 100%;
  }
  .section_2 {
    padding: 2.67rem 2.44rem 0;
    background-color: #121212;
    overflow: hidden;
  }
  .text_7 {
    color: #ffffff;
    font-size: 3.5rem;
    font-family: "Noto Serif SC", serif;
    font-weight: 700;
    line-height: 3.34rem;
  }
  .text_8 {
    margin-top: 3rem;
    color: #ffffff;
    font-size: 1rem;
    font-family: kaiti;
    line-height: 1rem;
  }
  .group_2 {
    margin-top: 3rem;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }
  .image {
    border-radius: 2rem;
    height: 20rem;
    margin-bottom: 0.84rem;
  }
  .section_3 {
    padding: 2rem 10rem 2rem 10rem;
    background-color: #383838;
    overflow: hidden;
  }
  .view {
    margin-top: 1.86rem;
  }
  .font_2 {
    font-size: 1.5rem;
    font-family: kaiti;
 
    color: #ffffff;
  }
  .align-center {
    align-items: center;
  }
  .justify-center {
    justify-content: center;
  }
  .group_3 {
    padding: 3rem 0 4rem;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }
  .tabs-header {
    background-color: #121212;
    overflow: hidden;
  }
  .view_2 {
    margin-left: 2.44rem;
    margin-right: 2.44rem;
  }
  .section_4 {
    background-color: #121212;
    overflow: hidden;
    width: 100%;
  }
</style>
