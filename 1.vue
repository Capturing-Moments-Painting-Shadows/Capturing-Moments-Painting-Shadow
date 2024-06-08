<template>
  <div class="flex-col page">
    <div class="flex-row justify-between items-center header">
      <div class="flex-row items-center">
        <div class="flex-col justify-start text-wrapper"><span class="text">凝时绘影</span></div>
        <div class="flex-row group_1 ml-40-5">
          <span class="font" @click="navigateToRoute(0)">主页</span>
          <div class="flex-row shrink-0 group_6 ml-31-5">
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
    <div class="flex-col group section">
      <div class="flex-col section_2">
        <span class="self-center text_7">相册展示</span>
        <span class="self-center text_8">这里展示了我们最新的相册作品</span>
        
        <div class="album-container">
          <div v-for="category in categories" :key="category.id" class="album-item" @click="navigateToAlbum(category.id)">
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

<script setup>
import { useRouter } from 'vue-router';
import { ref, reactive, onMounted } from 'vue';
import axios from 'axios';

const props = defineProps({});

const categories = ref([]);

const router = useRouter();

const routes = [
  'zhuye', 
  'denglu', 
  'leibiechuangjian', 
  'zhaopianshangchuan',
  'xiangcezhanshi',
  'Page_group_tuxiangshengcheng', 
  'zhaopianzhanshi'
];

function navigateToRoute(index) {
  router.push({ name: routes[index] });
}

onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:5003/api/categories')
      categories.value = response.data;
  } catch(error) {
    console.error('Error loading categories:', error);
  };
});

function navigateToAlbum(albumId) {
  router.push({ name: 'zhaopianzhanshi', params: { id: albumId } });
}
</script>

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
  .album-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }
  .album-item {
    width: 30%;
    margin-bottom: 2rem;
    position: relative;
    cursor: pointer;
  }
  .image {
    width: 100%;
    border-radius: 2rem;
    height: 20rem;
    object-fit: cover;
  }
  .font_2 {
    font-size: 1.5rem;
    font-family: kaiti;
    color: #ffffff;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: rgba(0, 0, 0, 0.5);
    padding: 0.5rem 1rem;
    border-radius: 1rem;
  }
</style>
