// /*
// Uses Formik package to make things pretty and easy
// https://formik.org/docs/tutorial

// */
// import React from "react";
// import { FormChildLoc, Common } from "../Components/Localization";
// import { useFormik } from 'formik';

// //FormChildLoc.setLanguage('uk'); //Only changes this obj's lang TODO

// const validate = values => {
//     const errors = {};

//     if (!values.firstName) {
//         errors.firstName = Common.Required;
//     } /*else if (values.firstName.length > 15) {
//     errors.firstName = 'Must be 15 characters or less';
//     }*/

//     if (!values.lastName) {
//         errors.lastName = Common.Required;
//     }

//     if (!values.email) {
//         errors.email = Common.Required;
//     } else if (!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(values.email)) {
//         errors.email = 'Invalid email address';
//     }

//     return errors;
// };

// const FormChild = () => {
//     const formik = useFormik({
//         initialValues: {
//         firstName: '',
//         lastName: '',
//         email: '',
//         },
//         validate,
//         onSubmit: values => {
//             alert(JSON.stringify(values, null, 2));
//         },
//     });
//     return (
//     <form onSubmit={formik.handleSubmit}>
//         <h3>{FormChildLoc.ChildNameSuperLabel}</h3>
//         <label htmlFor="firstName">{FormChildLoc.FirstName}</label>
//         <input
//             id="firstName"
//             name="firstName"
//             type="text"
//             onChange={formik.handleChange}
//             onBlur={formik.handleBlur}
//             value={formik.values.firstName}
//         />
//         {formik.errors.firstName ? <div>{formik.errors.firstName}</div> : null}

//         <label htmlFor="lastName">{FormChildLoc.FirstName}</label>
//         <input
//             id="lastName"
//             name="lastName"
//             type="text"
//             onChange={formik.handleChange}
//             onBlur={formik.handleBlur}
//             value={formik.values.lastName}
//         />
//         {formik.errors.lastName ? <div>{formik.errors.lastName}</div> : null}

//         <br/>
//         {/*Remove THis Later*/}
//         <label htmlFor="email">Email Address</label>
//         <input
//         id="email"
//         name="email"
//         type="email"
//         onChange={formik.handleChange}
//         onBlur={formik.handleBlur}
//         value={formik.values.email}
//         />
//         {formik.errors.email ? <div>{formik.errors.email}</div> : null}

//         <button type="submit">{FormChildLoc.SubmitForm}</button>
//     </form>
//     );
// };

// export default FormChild;