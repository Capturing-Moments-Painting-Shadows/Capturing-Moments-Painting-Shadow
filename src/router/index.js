import { createRouter, createWebHistory } from 'vue-router';
import Zhuye from '../pages/zhuye/zhuye.vue';
import Denglu from '../pages/denglu/denglu.vue';
import Zhuce from '../pages/zhuce/zhuce.vue';
import Leibiechuangjian from '../pages/leibiechuangjian/leibiechuangjian.vue';
import Zhaopianshangchuan from '../pages/zhaopianshangchuan/zhaopianshangchuan.vue';
import Xiangcezhanshi from '../pages/xiangcezhanshi/xiangcezhanshi.vue';
import Zhaopianzhanshi from '../pages/zhaopianzhanshi/zhaopianzhanshi.vue';
import Zhaopiancaozuo from '../pages/zhaopiancaozuo/zhaopiancaozuo.vue';
import Page_group_tuxiangshengcheng from '../pages/Page_group_tuxiangshengcheng/Page_group_tuxiangshengcheng.vue';

const routes = [
  {
    path: '/',
    name: 'zhuye',
    component: Zhuye,
  },
  {
    path: '/denglu',
    name: 'denglu',
    component: Denglu,
  },
  {
    path: '/zhuce',
    name: 'zhuce',
    component: Zhuce,
  },
  {
    path: '/leibiechuangjian',
    name: 'leibiechuangjian',
    component: Leibiechuangjian,
  },
  {
    path: '/zhaopianshangchuan',
    name: 'zhaopianshangchuan',
    component: Zhaopianshangchuan,
  },
  {
    path: '/xiangcezhanshi',
    name: 'xiangcezhanshi',
    component: Xiangcezhanshi,
  },
  {
    path: '/zhaopianzhanshi',
    name: 'zhaopianzhanshi',
    component: Zhaopianzhanshi,
  },
  {
    path: '/zhaopiancaozuo',
    name: 'zhaopiancaozuo',
    component: Zhaopiancaozuo,
  },
  {
    path: '/Page_group_tuxiangshengcheng',
    name: 'Page_group_tuxiangshengcheng',
    component: Page_group_tuxiangshengcheng,
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;