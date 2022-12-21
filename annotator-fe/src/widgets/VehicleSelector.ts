export default function (args: any) {
  const currentSelectionBody = args.annotation
    ? args.annotation.bodies.find(function (b: any) {
        return b.purpose == "tagging";
      })
    : null;

  const currentSelectionValue = currentSelectionBody
    ? currentSelectionBody.value
    : null;

  const addTag = function (value: string) {
    if (currentSelectionBody) {
      args.onUpdateBody(currentSelectionBody, {
        type: "TextualBody",
        purpose: "tagging",
        value,
      });
    } else {
      args.onAppendBody({
        type: "TextualBody",
        purpose: "tagging",
        value,
      });
    }
  };

  const createOption = function (
    label: string,
    value: string,
    select: HTMLSelectElement
  ) {
    const option = document.createElement("option");
    option.setAttribute("value", value);
    const t = document.createTextNode(label);
    option.appendChild(t);
    select.appendChild(option);
    if (value == currentSelectionValue) {
      select.value = value;
    }
    return option;
  };

  const container = document.createElement("div");
  const select = document.createElement("select");
  select.setAttribute("name", "tagSelect");
  createOption("Select Vehicle", "", select);
  createOption("Car", "car", select);
  createOption("Bus", "bus", select);
  createOption("Autorikshaw", "autorikshaw", select);
  createOption("Bike", "bike", select);

  container.appendChild(select);

  select.addEventListener("change", () => {
    addTag(select.value);
  });
  return container;
}
