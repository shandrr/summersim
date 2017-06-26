# 
# @author Jake Runyan 
# @git www.github.com/runyanjake/summersim
# @file /summergame/neuralnet.py
# Uses Google Tensorflow: https://www.youtube.com/watch?v=2FmcHiLCwTU
# 

#LIBRARY IMPORTS
import tensorflow as tf

#LOCAL IMPORTS


#NNET HYPERPARAMETERS (set to defaults)
learning_rate = 0.01 		#slow learning is fine
training_iteration = 100	#number of training loops, more -> accuracy
batch_size = 1000			#number of sets to train
display_step = 2			#idk

#architecture of nnet (set to defaults)
num_inputs = 10
num_outputs = 4


#FUNCTIONS

def set_learning_rate(lr):
	learning_rate = lr

def set_training_iteration(ti):
	training_iteration = ti

def set_batch_size(bs):
	batch_size = bs

def set_display_step(ds):
	display_step = ds

#constructor
#@pre make sure hyperparams are set up before this is run.
def newneuralnet(): #note this should be split into the other methods.
	#create inputs
	x = tf.placeholder("float", [num_inputs]) 	#any-dimensional arr of inputs, modify accordingly
	#create outputs
	y = tf.placeholder("float", [num_outputs])	#any-dim arr of output actions, modify accordingly
	#weights 
	w = tf.Variable(tf.zeroes([num_inputs, num_outputs]))
	#bias
	b = tf.Variable(tf.zeroes([num_outputs]))
	#math model, for now something linear
	with tf.name_scope("Wx_b") as scope:
		model = tf.nn.softmax(tf.mathmul(x, w) + b)
	#summary operations so we can see what happenes
	w_h = tf.histogram_summary("weights", w)
	b_h = tf.histogram_summary("biases", b)
	#cost function
	with tf.name_scope("cost_function") as scope:
		#using cross entropy (should we do this?)
		cost_function = -tf.reduce_sum(y*tf.log(model))
		#summary to monitor the cost
		tf.scalar_summary("cost_function", cost_function)
	#optimization function, using gradient descent to find local minima
	with tf.name_scope("train") as scope:
		optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_function)
	#turn on the variables
	init = tf.initialize_all_variables()
	#merge all the summaries into something readable
	merged_summary = tf.merge_all_summaries()

	#RUN IT
	#initialize a session 
	with tf.Session as sess:
		sess.run(init)
		#set up summary writing output folder, we'll read from here later
		summary_writer = tf.train.SummaryWriter('./tensorflow_logs', graph_def=sess.graph_def)
		#training cycle
		for iteration in range(training_iteration):
			avg_cost = 0.
			#TODO 
			#total_batch = int(mnist.train.num_examples/batch_size) #mnist is the data in mnist format
			# Loop over all batches
			#TODO ALL OF LOOP:
        	#for i in range(total_batch):
        	    ##batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        	    # Fit training using batch data
        	    ##sess.run(optimizer, feed_dict={x: batch_xs, y: batch_ys})
        	    # Compute the average loss
        	    ##avg_cost += sess.run(cost_function, feed_dict={x: batch_xs, y: batch_ys})/total_batch
        	    # Write logs for each iteration
        	    ##summary_str = sess.run(merged_summary_op, feed_dict={x: batch_xs, y: batch_ys})
        	    ##summary_writer.add_summary(summary_str, iteration*total_batch + i)
        	# Display logs per iteration step
        	#TODO IFSTATEMENT
        	#if iteration % display_step == 0:
        	    #print "Iteration:", '%04d' % (iteration + 1), "cost=", "{:.9f}".format(avg_cost)


#destructor
def destroyneuralnet(nnet):
	print('destroyneuralnet TODO')

#adds input node to neural net
def add_input_node():
	num_inputs = num_inputs + 1

#removes input node to neural net
def remove_input_node():
	num_inputs = num_inputs - 1

#adds hidden node to neural net
def add_hidden_node():
	print('add_hidden_node TODO')

#adds output node to neural net
def add_output_node():
	num_outputs = num_outputs + 1

#removes output node to neural net
def remove_output_node():
	num_outputs = num_outputs - 1

#sets the smoothing function for output nodes
def set_smoothing_function(id):
	print('set_smoothing_function TODO')