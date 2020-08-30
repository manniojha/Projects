package sortvisualiser.algorithms;

import sortvisualiser.SortArray;

public class QuickSort implements ISortAlgorithm {

    private long stepDelay = 30;
    /**
     * This is where the magic of quick sort append.
     *
     * @param array this is the array to cut and merge
     * @param lowIndex the most left index of the array
     * @param highIndex  the most right index of the array
     * @see SortArray
     */
    private int findPivotPoint(SortArray array, int lowIndex, int highIndex) {
        int pivotValue = array.getValue(highIndex);
        int i = lowIndex - 1;
        for (int j = lowIndex; j <= highIndex - 1; j++) {
            if (array.getValue(j) <= pivotValue) {
                i++;
                array.swap(i, j, getDelay(), true);
            }
        }
        array.swap(i + 1, highIndex, getDelay(), true);
        return i + 1;
    }

    /**
     * This is the core of the algorithm quick sort.
     *
     * @param array this is the array to cut and merge
     * @param lowIndex the most left index of the array
     * @param highIndex  the most right index of the array
     * @see SortArray
     */
    private void quickSort(SortArray array, int lowIndex, int highIndex) {
        if (lowIndex < highIndex) {
            int pivotPoint = findPivotPoint(array, lowIndex, highIndex);
            quickSort(array, lowIndex, pivotPoint - 1);
            quickSort(array, pivotPoint + 1, highIndex);
        }
    }

    @Override
    public void runSort(SortArray array) {
        quickSort(array, 0, array.arraySize() - 1);
    }

    @Override
    public String getName() {
        return "Quick Sort";
    }

    @Override
    public long getDelay() {
        return stepDelay;
    }

    @Override
    public void setDelay(long delay) {
        this.stepDelay = delay;
    }

}
