<template>
  <div class="mt-16 w-100">
    <div class="d-flex pa-8 align-center">
      <div class="w-50">
        <v-file-input
          small-chips
          multiple
          label="Choose files"
          v-model="files"
          accept="image/*"
        ></v-file-input>
      </div>
      <v-spacer></v-spacer>
      <v-btn @click="upload" :disabled="!files">Upload</v-btn>
    </div>
    <v-row class="ma-0 pa-8">
      <v-col
        v-for="image in images"
        :key="image.id"
        cols="12"
        sm="6"
        md="4"
        lg="3"
      >
        <v-img
          @click="$router.push(`/image/${image.id}`)"
          :src="imageUrl(image)"
        ></v-img>
      </v-col>
    </v-row>
  </div>
</template>
<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import type { Ref } from "vue";
import { useRoute } from "vue-router";
import { listImages, postImages } from "@/api/images";
const BASE_URL = "http://localhost:8005/";
export default defineComponent({
  setup() {
    const route = useRoute();
    const images: Ref<any[]> = ref([]);
    const files: Ref<any> = ref(null);

    const upload = async () => {
      const formData = new FormData();
      files.value.forEach((file: any) => {
        formData.append("files", file);
      });
      try {
        await postImages(route.params.projectId as string, formData);
        window.location.reload();
      } catch (error) {
        alert("An error occured");
      }
    };
    const imageUrl = (image: any) => {
      const parts = image.name.split(".");
      const format = parts[parts.length - 1];
      return `${BASE_URL}projects/${route.params.projectId}/${image.id}.${format}`;
    };
    onMounted(async () => {
      if (route.params.projectId) {
        try {
          const res = await listImages(route.params.projectId as string);
          images.value = res.data.images;
        } catch (error) {
          alert("Error occured");
        }
      }
    });

    return { images, files, upload, imageUrl };
  },
});
</script>
