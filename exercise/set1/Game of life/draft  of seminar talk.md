 Topics: Evolution in sexual and asexual populations

**The background of the topic:**
 
Question:
Although most species on the planet reproduce sexually, why do some species still reproduce asexually? Why is it evolutionarily beneficial for some species to require two parents to produce offspring and others only one?

2 types of reproduction are asexual and sexual.  Asexual reproduction is when an organism makes a genetically identical clone of itself. Most simplest life form such as bacteria reproduce in this manner

Sexual reproduction is much more complex and involves two members of a species coming together to produce genetically distinct offspring. e.g. Human, birds

Sexual and asexual population use different strategy to help them survive. 

For asexual population, their advantage is energy-saving because they don't need the other gender individuals to give birth to the offsprings.  e.g. microrganism

But the advantage of sexual creature is obious, the evolution speed of  sexual creatures are larger than that of asexual creatures due to gene recombination.

**1.clonal interference**

In an asexual population, two beneficial mutants can be incorporated into the population only if the second occurs in a descendant of the individual in which the first occurred. On the other hand, in a sexual population the various mutants can get into the same individual by recombination. Only if the mutation rate were so low or the population so small that each mutant became established before another favorable mutant occurred would the two systems be equivalent. [cite]

Two pictures here.

Mathematical formulation of clonal interference

Let N = the population number
U = the total rate of occurrence per individual per generation of favorable mutations at all loci
g = the average number of generations between the occurrence of a favorable mutation and the occurrence of another favorable mutation in a descendant of the first
x = 1/U = the number of individuals such that on the average one favorable mutation will occur
s = the average selective advantage of a favorable mutant

After the mathematical derivations, we get the formula of the average number of generations g by s,U, and N in asexual population.

The total number of favorable mutations in sexual population after g generations is NUg.

So the ratio of incorporated mutations in a sexual population to that in an asexual population is NUg:1

Interpret the table and formula.
1. The advantage of recombination is negligible in a small population (10^3) and small U/s, but it will be obvious in a large population and large U/s
2. Table 1 also shows that the advantage of recombination increases with an increase in the population size. In fact, with large populations the advantage is nearly proportional to the population number.
3. It's interesting that U and s enter the formula  always in the form U/s

**2.Rate of Adaptation in Sexuals and Asexuals, A solvable Model of the Fisher-Muller Effect**

Question:
What's the difference of sexual and asexual reproduction in genetic level? How can we find a model to describe the evolution process of sexual and asexual reproduction in genetic level?

As we mentioned before, the asexual reproduction is making a genetically identical clone of itself but the sexual reproduction need two members of species coming together and produce a genetically distinct offspring. The reason why the two different ways of reproduction making different genetically result is that genetic recombination occurs during the sexual reproduction but the other one not.

For a general evolution process, selection and mutation should be considered. Here we choose the Wright-Fisher model to describe this process. We also need to find the way to describe the process of recombination.

The assumption of models are:
1. Assuming the all mutations are beneficial and additive
2. We only consider the effect of  two loci's genes on the individual's fitness
3. We assume no epistasis among the mutations

let $f_t(n1,n2)$ denote the frequency of all genotypes with $n_1$ mutations at first locus and n2 mutations at the second locus at generation t. 

After selection
$f^s_t{n1,n2} = \frac{e^{s_1n_1+s_2n_2}}{\overline w_t} $
where
$$\overline w_t = \sum_{n_1,n_2}e^{s_1n_1+s_2n_2}f_t(n1,n2)$$

After mutation:

formula....

Introduce the R(n1,n2|k1,k2;l1,l2) to be the probability that resulting offspring of two indiviuals with respective genotypes (k1,k2) and (l1,l2) has the genotype (n1,n2)

r's meaning

After recombination

formula....

After simulation of the models, introduce the speed of evolution $$v = \lim_{t \rightarrow \infty} \frac{ln \overline w_t}{t}$$

**statistical results and simulation results in infinite population**

The evolution speed of sexual population is $v_s = s_1+s_2$ and that of asexual population is $v_a = max{s_1,s_2}$. This can be interpreted by the clonal interference

The evolution speed of sexual population is twice as that of asexual population in infinite population if $s_1 = s_2$ 

In the model, we take the recombination rate *r* as a parameter. If we set r very small to 10^{-9}, the evolution speed of it will be same as that of obligate sexual (r = 1) in infinite population.

The explanation of this pheonomenon is that it always has the probability to recombine the genes of two individuals which have the largest number of mutations in each generation in infinite population. Selection effect will works and drift the average fitness of the whole population to the direction of the most fitness individual.

**statistical results and simulation results in finite population**

Formula between the population size N, evolution speed $v^{RBW}_a$, mutation rate U and selection coefficient s in asexual popution [cite]

Dispaly the figures of simulation comparing the analytical formula given above

Apply the travelling wave approach to the finite population, get the final formula and compare it with the simulation result. It can fit the simulation result in the large population scale. Even though it can't fit simulation result really well, we can still get some insight by this model.

Display the figure of the ratio of $v_s(r,U)$ to $v_a(U/2)$ at half mutation rate in different recombination rate *r* from 0 to 1

We can find the ratio increases with the recombination rate *r*

Display the figure of the ratio of $v_s(r,U)$ to $v_a(U)$ at same mutation rate in different recombination rate *r* from 0 to 1 

Multiple-site mutations

....