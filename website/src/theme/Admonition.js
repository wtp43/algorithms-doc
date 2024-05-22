import React from "react";
import Admonition from "@theme-original/Admonition";

export default function AdmonitionWrapper(props) {
  if (
    props.type !== "note" ||
    props.type !== "tip" ||
    props.type !== "info" ||
    props.type !== "warning" ||
    props.type !== "danger"
  ) {
    return <Admonition title={props.title} type="tip" {...props} />;
  }
  return <Admonition {...props} />;
}
