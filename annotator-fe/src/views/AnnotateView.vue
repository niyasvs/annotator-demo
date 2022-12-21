<template>
  <div class="mt-16 w-100 pa-8">
    <div class="d-flex align-center justify-center">
      <span>View</span
      ><v-switch
        v-model="isAnnotate"
        class="switch mx-4"
        hide-details
        label=""
        inset
        @change="onToggleSwitch"
      ></v-switch
      ><span>Annotate</span>
    </div>
    <img id="annotateImg" :src="imageUrl" alt="" />

    <div class="d-flex">
      <v-btn @click="reset">Reset</v-btn>
      <v-spacer></v-spacer>
      <v-btn @click="downloadCsv">Download CSV</v-btn>
      <v-btn @click="save">Save</v-btn>
    </div>
  </div>
</template>
<script lang="ts">
import { getImage, saveAnnotation } from "@/api/images";
import { computed, defineComponent, onMounted, ref } from "vue";
import type { Ref } from "vue";
import { useRoute } from "vue-router";
import { Annotorious } from "@recogito/annotorious";
import "@recogito/annotorious/dist/annotorious.min.css";
import VehicleSelectorWidget from "@/widgets/VehicleSelector";

const BASE_URL = "http://localhost:8005/";

export default defineComponent({
  setup() {
    const route = useRoute();
    const image: Ref<any> = ref({});
    const isAnnotate = ref(false);
    const imageUrl = computed(() => {
      if (image.value.id) {
        const parts = image.value.name.split(".");
        const format = parts[parts.length - 1];
        return `${BASE_URL}projects/${image.value.project}/${image.value.id}.${format}`;
      }
      return "";
    });
    const anno = ref({} as any);
    const save = async () => {
      await saveAnnotation(
        route.params.imageId as string,
        anno.value.getAnnotations()
      );
      alert("Saved");
    };
    const reset = () => {
      anno.value.clearAnnotations();
    };
    const onToggleSwitch = () => {
      anno.value.readOnly = !isAnnotate.value;
    };
    const downloadCsv = () => {
      const annotations = anno.value.getAnnotations();
      const csvData: any[] = [["File", "A", "B", "C", "D"]];
      annotations.forEach((annotation: any) => {
        const val = annotation.target.selector.value;
        const pos = val.split("xywh=pixel:")[1].split(",");
        csvData.push([`${image.value.project}/${image.value.name}`, ...pos]);
      });

      let csvContent =
        "data:text/csv;charset=utf-8," +
        csvData.map((e) => e.join(",")).join("\n");
      var encodedUri = encodeURI(csvContent);
      var link = document.createElement("a");
      link.setAttribute("href", encodedUri);
      link.setAttribute("download", "annotation.csv");
      document.body.appendChild(link);

      link.click();
    };
    onMounted(async () => {
      if (route.params.imageId) {
        try {
          const res = await getImage(route.params.imageId as string);
          image.value = res.data;

          anno.value = new Annotorious({
            image: "annotateImg",
            widgets: [VehicleSelectorWidget],
          });
          anno.value.readOnly = true;
          for (const annotation of image.value.annotations) {
            anno.value.addAnnotation(annotation);
          }
        } catch (error) {
          alert("Error occured");
        }
      }
    });
    return {
      imageUrl,
      save,
      reset,
      isAnnotate,
      onToggleSwitch,
      downloadCsv,
    };
  },
});
</script>

<style scoped>
#annotateImg {
  height: auto;
  width: 600px;
}
.switch {
  max-width: 48px;
}
</style>
