<template>
  <div>
    <img
      src="https://www.gstatic.com/webp/gallery/1.jpg"
      id="imagetest"
      alt=""
    />
    <button @click="saveAnnotations">Save</button>
  </div>
</template>
<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import { Annotorious } from "@recogito/annotorious";
import "@recogito/annotorious/dist/annotorious.min.css";
import VehicleSelectorWidget from "@/widgets/VehicleSelector";
export default defineComponent({
  setup() {
    const anno = ref({} as any);
    onMounted(() => {
      anno.value = new Annotorious({
        image: "imagetest",
        widgets: [VehicleSelectorWidget],
      });
    });
    const saveAnnotations = () => {
      console.log(anno.value.getAnnotations());
    };
    return { saveAnnotations };
  },
});
</script>
