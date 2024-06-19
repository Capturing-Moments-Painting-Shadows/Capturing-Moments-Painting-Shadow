<script setup>
  import { useRouter } from 'vue-router';
  import { ref, reactive, computed, onMounted } from 'vue';
  import { useStore } from 'vuex';
  import axios from 'axios';

  const data = reactive({
    title: '',
    file: null
  });

  const AUTO_CATEGORY_ID = 'auto'; // 特殊ID用于自动分类

  function triggerFileInput() {
    const fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = 'image/*';
    fileInput.addEventListener('change', handleFileUpload);
    fileInput.click();
  }

  const selectedCategory = ref('');
  const categories = ref([]);

  const store = useStore();
  const router = useRouter();

  const isAuthenticated = computed(() => store?.state?.isAuthenticated || false);
  const username = computed(() => store?.state?.username || '未登录');

  function onClick(routeName) {
    router.push({ name: routeName });
  }

  function handleFileUpload(event) {
    data.file = event.target.files[0];
  }

  async function uploadPhoto() {
    if (!isAuthenticated.value) {
      alert('请先登录');
      return;
    }

    if (!data.file) {
      alert('请先选择一张照片');
      return;
    }

    const formData = new FormData();
    formData.append('username', username.value);
    formData.append('title', data.title);
    formData.append('category_id', selectedCategory.value);
    formData.append('file', data.file);

    try {
      const response = await axios.post('http://localhost:5003/upload_photos', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      if (response && response.data) {
        if (response.status === 200) {
          alert('上传成功！');
        } else {
          console.error('Unexpected response format:', response);
        }
      }
    } catch (error) {
      if (error.response && error.response.data) {
        console.error('Error response data:', error.response.data);
        alert(error.response.data.message);
      } else {
        console.error('Unexpected error:', error);
      }
    }
  }

  onMounted(async () => {
    try {
      const response = await axios.get('http://localhost:5003/select_categories', {
        params: {
          username: username.value
        }
      });
      categories.value = response.data;
      categories.value.push({ id: AUTO_CATEGORY_ID, name: '自动分类' });
    } catch (error) {
      console.error('Error fetching categories:', error);
    }
  });
</script>

<template>
  <div class="flex-col page">
    <div class="flex-row justify-between items-center header">
      <div class="flex-row items-center">
        <div class="flex-col justify-start text-wrapper">
          <span class="text">凝时绘影</span>
        </div>
        <div class="flex-row ml-81">
          <span class="font text_3 ml-53" @click="onClick('zhuye')">主页</span>
          <div class="flex-row ml-63">
            <span class="font text_3 ml-53" @click="onClick('denglu')">登录注册</span>
            <span class="font text_3 ml-53" @click="onClick('leibiechuangjian')">类别创建</span>
            <span class="font text_3 ml-53" @click="onClick('zhaopianshangchuan')">照片上传</span>
            <span class="font text_3 ml-53" @click="onClick('Page_group_tuxiangshengcheng')">图像生成</span>
            <span class="font text_3 ml-53" @click="onClick('xiangcezhanshi')">相册展示</span>
          </div>
        </div>
      </div>
      <div>
        <span class="font text_3 ml-53">{{ isAuthenticated ? username : '未登录' }}</span>
      </div>
    </div>
    <div class="flex-col section section_2">
      <img class="image" src="https://picture.gptkong.com/20240610/00151fabba8f27475d88f0937be074b23f.png" />
      <div class="flex-col section_3 mt-20">
        <div class="flex-col self-center">
          <span class="self-start text_7">凝时绘影 照片上传</span>
          <span class="self-center text_8 mt-21">请上传您的照片并指定类别</span>
        </div>
        <div class="flex-col self-stretch justify-between items-center section group_2">
          <span class="self-start font text_9">照片标题</span>
          <el-input class="input mt-14" v-model="data.title"></el-input>
        </div>
        <div class="flex-col self-stretch section group_3">
          <span class="self-start justify-between font text_11">类别</span>
          <div class="flex-row justify-between items-center section_5 mt-14">
            <div class="flex-col justify-start items-end group_1">
              <select v-model="selectedCategory" class="input mt-14">
                <option value="" disabled>选择照片分类</option>
                <option v-for="category in categories" :key="category.id" :value="category.id">
                  {{ category.name }}
                </option>
              </select>
            </div>
          </div>
        </div>
        <div class="flex-col justify-start self-stretch group_5">
          <span class="font text_13">凝时绘影 照片上传</span>
          <img class="image_5 mt-14" src="https://picture.gptkong.com/20240609/0432d2943f603b4fca82a7995c306b43ee.png" @click="triggerFileInput" />
        </div>
        <div @click="uploadPhoto" class="flex-col justify-start items-center self-stretch text-wrapper_2">
          <span class="text_14">上传照片</span>
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
    cursor: pointer;
  }
  .text {
    margin-left: 0.22rem;
    margin-right: 0.21rem;
    color: #ffffff;
    font-size: 1.38rem;
    font-family: "Noto Serif SC", serif;
    font-weight: 700;
  }
  .font {
    font-size: 1rem;
    font-family: "Noto Serif SC", serif;
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
    font-family: "Noto Serif SC", serif;
    font-weight: 700;
    line-height: 3.5rem;
    text-align: center;
    width: 30rem;
    height: 3.5rem;
  }
  .text_8 {
    color: #ffffff;
    font-size: 1.13rem;
    font-family: "Noto Serif SC", serif;
    line-height: 1.06rem;
  }
  .group_2 {
    margin-top: 4.52rem;
  }
  .text_9 {
    line-height: 0.91rem;
    width: 30rem;
  }
  .input {
    align-self: stretch;
    border-radius: 0.75rem;
  }
  .group_3 {
    margin-top: 2.76rem;
  }
  .text_11 {
    line-height: 0.91rem;
    width: 30rem;
  }
  .section_5 {
    background-color: #383838;
    border-radius: 0.75rem;
    overflow: hidden;
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
    margin-right: 3rem;
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
    padding: 0.99rem 0 1.09rem;
    border-radius: 0.75rem;
  }
  .text-wrapper_2 {
    margin-top: 3rem;
    padding: 0.99rem 0 1.09rem;
    background-color: #800080;
    border-radius: 0.75rem;
    cursor: pointer;
    text-align: center;
  }
  .text_14 {
    color: #ffffff;
    font-size: 1.25rem;
    font-family: "Noto Serif SC", serif;
    line-height: 1.17rem;
  }
</style>
