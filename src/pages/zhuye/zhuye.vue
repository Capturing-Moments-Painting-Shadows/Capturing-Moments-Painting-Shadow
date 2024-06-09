<script setup>
  import { useRouter } from 'vue-router';
  import { computed } from 'vue';
  import { useStore } from 'vuex';

  const props = defineProps({});

  const router = useRouter();
  const store = useStore();

  // 确保 store 已经初始化并且 state 存在
  const isAuthenticated = computed(() => store?.state?.isAuthenticated || false);
  const username = computed(() => store?.state?.username || '未登录');
  
  const checkAuthAndNavigate = (routeName) => {
    if (!isAuthenticated.value) {
      alert('请先登录');
      router.push({ name: 'denglu' });
    } else {
      router.push({ name: routeName });
    }
  };

  function onClick() {
    router.push({ name: 'zhuye' });
  }

  function onClick_1() {
    router.push({ name: 'denglu' });
  }

  function onClick_2() {
    checkAuthAndNavigate('leibiechuangjian');
  }

  function onClick_3() {
    checkAuthAndNavigate('zhaopianshangchuan');
  }

  function onClick_4() {
    checkAuthAndNavigate('Page_group_tuxiangshengcheng');
  }

  function onClick_5() {
    checkAuthAndNavigate('xiangcezhanshi');
  }
</script>

<template>
  <div class="flex-col page">
    <div class="flex-row justify-between items-center section">
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
    <div class="flex-col justify-start items-center relative section_3">
      <img
        class="shrink-0 image"
        src="https://picture.gptkong.com/20240610/00139850a2c0fa4d15be2ed0335f3a0efd.png"
      />
      <div class="flex-col justify-start items-center mask section_2">
        <div class="flex-col items-center">
          <span class="text_7">凝时绘影</span>
          <span class="text_8 mt-38">
            凝时绘影是一个功能强大的照片管理系统，帮助用户轻松管理和分类照片，同时提供自动分类和图像生成功能。
          </span>
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
    padding-bottom: 4.81rem;
    background-color: #000000;
    width: 100%;
    overflow-y: auto;
    overflow-x: hidden;
    height: 100%;
  }
  .section {
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
  .section_3 {
    background-color: #121212;
    overflow: hidden;
  }
  .image {
    width: 100vw;
    height: 49.3056vw;
  }
  .mask {
    position: absolute;
    left: 0;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
  }
  .section_2 {
    padding: 20.98rem 0 24.56rem;
    background-color: #00000033;
    backdrop-filter: blur(0.31rem);
  }
  .text_7 {
    color: #ffffff;
    font-size: 5rem;
    font-family: "Noto Serif SC", serif;
    font-weight: 700;
    line-height: 4.67rem;
  }
  .text_8 {
    color: #ffffff;
    font-size: 1.13rem;
    font-family: "Noto Serif SC", serif;
    line-height: 1.14rem;
  }
</style>
