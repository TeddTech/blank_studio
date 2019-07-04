
// const app = new Vue({
// 	'el': '#contact-form',

// 	data: {
// 		contact: {
// 			name: '',
// 			email: '',
// 			message: '',
// 		},

//         isSending: false,
//         step: false
// 	},

// 	methods: {

// 		/**
// 		 * Clear the form
// 		 */	
// 		clearForm() {
// 			for (let field in this.contact) {
// 				this.contact[field] = ''
// 			}
// 		},

// 		/**
// 		 * Handler for submit
// 		 */	
// 		onSubmit(evt) {
// 			evt.preventDefault();

// 			this.isSending = true;

// 			setTimeout(() => {
// 				// Build for data
// 				let form = new FormData();
// 				for (let field in this.contact) {
// 					form.append(field, this.contact[field]);
//                 }
                
//                 this.step = true;
//                 this.isSending = false;


// 				// Send form to server	
// 				// this.$http.post('/app.py', form).then((response) => {
// 				// 	console.log(response);
// 				// 	this.clearForm();
// 				// 	this.isSending = false;
// 				// }).catch((e) => {
// 				// 	console.log(e)
// 				// });

// 			}, 1000);
// 		}
// 	}

// });


// window.app = app;