<script setup>
  import { useRouter } from 'vue-router';
  import { ref, reactive, onMounted } from 'vue';
  import axios from 'axios';

  const props = defineProps({});

  const categories = ref([]);

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

  onMounted(async () => {
    try {
      const response = await axios.get('http://localhost:5003/api/categories')
        categories.value = response.data;
    } catch(error) {
        console.error('Error loading categories:', error);
      };
    });

  function navigateToAlbum(albumId, userId) {
    router.push({ name: 'zhaopianzhanshi', params: { category_id: albumId, user_id : userId } });
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
    </div>
    <div class="flex-col group section">
      <div class="flex-col section_2">
        <span class="self-center text_7">相册展示</span>
        <span class="self-center text_8">这里展示了我们最新的相册作品</span>
        <div class="album-container">
          <div v-for="category in categories" :key="category.id" class="album-item" @click="navigateToAlbum(category.id, 1)">
            <img 
              :src="category.path ? `http://localhost:5003/${category.path}` : 'https://ide.code.fun/api/image?token=6662d7b6a16e9e001251f0b6&name=9f5c087ce21f2c8cb52379d16e5ba492.png'" 
              class="image" 
            />
            <span class="font_2">{{ category.name }}</span>
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

  .section_3 {
    padding: 2rem 10rem 2rem 10rem;
    background-color: #383838;
    overflow: hidden;
  }
  .view {
    margin-top: 1.86rem;
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


  .album-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start; /* 确保不足三个的那一行靠左对齐 */
    gap: 2rem; /* 增加项目之间的间距 */
    margin-top: 4rem; /* 增加当前组件与上一个组件之间的距离 */
  }
  
  
  .album-item {
    width: 30%; /* 确保每行最多显示三个项目 */
    position: relative;
    cursor: pointer;
    text-align: center; /* 文字居中 */
  }
  
  .image {
    width: 100%;
    border-radius: 2rem;
    height: auto; /* 自动调整高度以保持比例 */
    object-fit: cover;
    display: block; /* 确保图片作为块级元素 */
  }
  
  .font_2 {
    display: block; /* 确保文字作为块级元素 */
    text-align: center; /* 文字居中 */
    font-size: 1.5rem;
    font-family: kaiti;
    color: #ffffff;
    background-color: rgba(0, 0, 0, 0.5); /* 半透明背景 */
    padding: 0.5rem 1rem;
    border-radius: 1rem;
    margin-top: 0.5rem; /* 增加文字与图片之间的间距 */
  }
  
  
</style>
