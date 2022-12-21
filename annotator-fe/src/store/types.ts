export type User = {
  name: string;
};

export type Image = {
  url: string;
  annotations: any[];
};

export type State = {
  user: User;
  images: Image[];
};
