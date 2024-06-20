<script setup>
import { useRouter } from 'vue-router';
import { reactive, ref, computed } from 'vue';
import { ElUpload, ElMessage, ElInput } from 'element-plus';
import { useStore } from 'vuex';
import axios from 'axios';

const props = defineProps({});

const data = reactive({
  v_model: '',
});

const imageUrl = ref('');
const filePath = ref('');
const router = useRouter();
const store = useStore();

const isAuthenticated = computed(() => store?.state?.isAuthenticated || false);
const username = computed(() => store?.state?.username || '未登录');

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

const handleSuccess = (response) => {
  imageUrl.value = `http://localhost:5003/${response.path}`;
  filePath.value = response.path;
};

const beforeUpload = (file) => {
  const isJPG = file.type === 'image/jpeg';
  const isLt2M = file.size / 1024 / 1024 < 2;

  if (!isJPG) {
    ElMessage.error('上传图片只能是 JPG 格式!');
  }
  if (!isLt2M) {
    ElMessage.error('上传图片大小不能超过 2MB!');
  }
  return isJPG && isLt2M;
};

const showUploaded = ref(false);

const handleClickUpload = () => {
  showUploaded.value = true;
};

const handleGenerateImage = async () => {
  if (!filePath.value || !data.v_model) {
    ElMessage.error('请先上传图片并输入图像名称');
    return;
  }
  
  try {
    const response = await axios.post('http://localhost:5003/generate_image', {
      username: username.value,
      category: '图像生成',
      imageName: data.v_model,
      filePath: filePath.value,
    });
    if (response.data.success) {
      ElMessage.success('图像生成成功');
    } else {
      ElMessage.error('图像生成失败');
    }
  } catch (error) {
    console.error('Error generating image:', error);
    ElMessage.error('图像生成失败');
  }
};
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

      <div>
        <span class="font text_3 ml-53">
          {{ isAuthenticated ? username : '未登录' }}
        </span>
      </div>
    </div>

    <div class="flex-col section section_2">
      <img
        class="image"
        src="https://picture.gptkong.com/20240610/001650992785d645a8aca8a6bdf6454d23.png"
      />
      <div class="flex-col items-center justify-center section_4">
        <span class="text_8">图像生成</span>
        <span class="text_9">上传图像并生成相似图片</span>
      </div>
      <div class="flex-row justify-center section_3 mt-29">
        <div class="flex-col justify-center items-center text-wrapper_2" @click="handleClickUpload">
          <el-upload
            class="upload-demo"
            action="http://localhost:5003/upload_temp"
            :show-file-list="false"
            :on-success="handleSuccess"
            :before-upload="beforeUpload"
            name="file"
          >
            <span v-if="!imageUrl" class="text_12">点击选择上传</span>
            <img v-if="showUploaded && imageUrl" :src="imageUrl" alt="uploaded image" class="uploaded-image"/>
          </el-upload>
        </div>
        <div class="flex-col justify-center items-center text-wrapper_2 ml-14">
          <span v-if="!generatedImageUrl" class="text_12">生成图像展示</span>
          <img v-if="generatedImageUrl" :src="generatedImageUrl" alt="generated image" class="uploaded-image"/>
        </div>
      </div>
      <div class="flex-row justify-center mt-29">
        <div class="flex-row group">
          <span class="self-start font text_10">图像名称</span>
          <el-input class="input elinput" v-model="data.v_model"></el-input>
        </div>
        <div class="flex-col justify-start items-center text-wrapper_5 ml-14" @click="handleGenerateImage">
          <span class="text_14">生成图像</span>
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
  .ml-14 {
    margin-left: 0.875rem;
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
    font-family: "Noto Serif SC", serif;
    font-weight: 700;
    line-height: 1.31rem;
  }
  .font {
    font-size: 1rem;
    font-family: "Noto Serif SC", serif;
    line-height: 0.93rem;
    color: #ffffff;
  }
  .text_2 {
    line-height: 0.94rem;
  }
  .text_3 {
    line-height: 0.94rem;
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
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 1.64rem 0 1.72rem;
    border-radius: 0.5rem;
    background-image: url('https://picture.gptkong.com/20240610/0016a1e361fa864f1891bacf915c0792fc.png');
    background-size: 100% 100%;
    background-repeat: no-repeat;
    width: 36.13rem;
    height: 33.38rem;
    cursor: pointer;
  }
  .text_12 {
    color: #ffffff;
    font-size: 2.25rem;
    font-family: "Noto Serif SC", serif;
    font-weight: 900;
    line-height: 2.02rem;
    text-align: center;
  }
  .section_4 {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 2rem;
  }
  .text_8 {
    color: #ffffff;
    font-size: 3rem;
    font-family: "Noto Serif SC", serif;
    font-weight: 700;
    line-height: 2.84rem;
  }
  .text_9 {
    margin-top: 2rem;
    color: #ffffff;
    font-size: 1.13rem;
    font-family: "Noto Serif SC", serif;
    line-height: 2rem;
  }
  .group {
    display: flex;
    align-items: center;
  }
  .text_10 {
    margin-right: 1rem;
    line-height: 2rem;
  }
  .input {
    width: 20rem !important;
    margin-right: 5rem;
    margin-bottom: 2rem;
  }
  .text-wrapper_5 {
    width: 20rem !important;
    background-color: #800080;
    border-radius: 0.75rem;
    text-align: center;
    cursor: pointer;
    height: 2rem;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .text_14 {
    color: #ffffff;
    font-size: 1.25rem;
    font-family: "Noto Serif SC", serif;
    line-height: 1.16rem;
  }
  .uploaded-image {
    width: 36.13rem;
    height: 33.38rem;
    object-fit: cover;
    border-radius: 0.5rem;
  }
</style>
