import Head from "next/head";
import Image from "next/image";
import styles from "../styles/Home.module.css";
import Checkbox from "@mui/material/Checkbox";

export default function Termsagreement() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Create Next App</title>
        <meta name="description" content="Generated by create next app" />
        <meta name="viewport" content="initial-scale=1, width=device-width" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={styles.main}>
        <p>
          File your report, and let Missing Children Europe's experts alert the
          police and their contacts. They will get in touch with you to safely
          return your missing child or children as soon as they're found.
        </p>
        <p>Testing</p>
        <button variant="contained" className={styles.startBtn}>
          Next
        </button>
      </main>
    </div>
  );
}
