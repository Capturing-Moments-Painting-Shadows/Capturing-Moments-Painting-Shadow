<script setup>
  import { useRoute, useRouter } from 'vue-router';
  import { ref, reactive, onMounted, computed } from 'vue';
  import axios from 'axios';

  import { ElButton, ElInput, ElMessageBox, ElMessage } from 'element-plus';
  import { useStore } from 'vuex';


  const props = defineProps({});

  const router = useRouter();
  const store = useStore();

  const isAuthenticated = computed(() => store?.state?.isAuthenticated || false);
  const username = computed(() => store?.state?.username || '未登录');
  const photo = computed(() => store?.state?.selectedPhoto || null)
  console.log(photo.value.file_path)
  const photo_path = photo.value.file_path

  const data = reactive({
    description: '',

    annotations: [],
    path:''
  });

  const photo_id = photo.value.id;

  onMounted(async () => {
    await fetchAnnotations();
  });

  async function fetchAnnotations() {
    try {
      const response = await axios.get(`http://localhost:5003/show_annotations?photo_id=${photo_id}`);
      data.annotations = response.data;
    } catch (error) {
      console.error('Failed to fetch annotations:', error);
    }
  }

  async function submitDescription() {
    if (data.description.trim()) {
      const newAnnotation = data.description.trim();
      const timestamp = new Date().toISOString();

      try {
        await axios.post('http://localhost:5003/save_annotation', {
          photo_id: photo_id,
          annotation: newAnnotation,
          timestamp: timestamp
        });
        ElMessage.success('提交成功');
        data.description = '';
        await fetchAnnotations();
      } catch (error) {
        ElMessage.error('提交注释失败');
        console.error('Failed to save annotation:', error);
      }
    }
  }

  async function deletePhoto() {
    try {
      await ElMessageBox.confirm('确定要删除这张照片吗?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      });
      const response = await axios.post('http://localhost:5003/delete_photo', { photo_id: photo_id });
      console.log(response.status)
      if (response.status == '200') {
        alert('照片删除成功');
        router.push({ name: 'zhaopianzhanshi' }); // 删除成功后跳转到照片界面
      } else {
        alert('照片删除失败');
      }
    } catch (error) {
      alert('照片删除失败');
      console.error('Failed to delete photo:', error);
    }
  }

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
      <div class="flex-row">
        <img
          class="shrink-0 image"

          :src="photo_path ? `http://localhost:5003/${photo_path}` : 'https://picture.gptkong.com/20240610/00138a0565ede2419f85b2148a2030c53a.png'" 
        />
        <div class="description-box">
          <div class="annotations-box">
            <ul>
              <li v-for="annotation in data.annotations" :key="annotation.id">
                {{ new Date(annotation.time).toLocaleString() }}: {{ annotation.annotation }}
              </li>
            </ul>
          </div>

        </div>
      </div>
      <div class="flex-row justify-between group mt-64">
        <div class="flex-row items-center">

          <span class="self-start text_7">{{photo.title}}</span>

        </div>
        <div class="flex-row group_2">
          <el-input v-model="data.description" class="elinput_1" placeholder="请在此处添加照片的注释..."></el-input>
          <el-button class="button elbutton" @click="submitDescription">提交注释</el-button>
          <el-button class="delete-button" @click="deletePhoto">删除图片</el-button>
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
    background-color: #000000;
    width: 100%;
    overflow-y: auto;
    overflow-x: hidden;
    height: 100%;
  }
  .header {
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
  .section {
    flex-grow: 1;
  }
  .section_2 {
    padding: 2rem 5rem 5rem;
    background-color: #121212;
    overflow: hidden;
    width: 100%;
  }
  .image {
    border-radius: 1rem;
    width: 50rem;
    height: 33rem;
    margin-right: 2rem; /* 图片和描述框之间的间距 */
  }
  .description-box {
    flex-grow: 1;
    color: #ffffff;
    font-size: 1.25rem;
    font-family: "Noto Serif SC", serif;
    line-height: 1.5rem;
    background-color: #333333;

    border-radius: 0.5rem;
  }
  .description-text {
    white-space: pre-wrap; /* 保留换行符 */
  }
  .group {
    padding-left: 0.24rem;
  }
  .text_7 {
    color: #ffffff;
    font-size: 3rem;
    font-family: "Noto Serif SC", serif;
    font-weight: 700;
    line-height: 2.81rem;

  }
  .delete-button {
    color: #ff4d4f;
    border-color: #ff4d4f;
  }
  .group_2 {
    display: flex;
    justify-content: space-between;
    align-items: center; /* 垂直居中对齐 */
    gap: 1rem;
  }
  .text_8 {
    color: #ffffff;
    font-size: 1.13rem;
    font-family: "Noto Serif SC", serif;

  }
  .elbutton {
    width: 7.5rem !important;
  }
  .elinput_1 {
    width: 40rem;
  }
</style>

